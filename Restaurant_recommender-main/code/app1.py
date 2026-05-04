import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors


app = Flask(__name__)  # initializing a flask app


import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "restaurant1_cleaned.csv")

if not os.path.exists(csv_path):
    raise FileNotFoundError(f"CSV file not found at: {csv_path}")


# Load the cleaned and enriched dataset
zomato_df = pd.read_csv(csv_path)

# Prepare the TF-IDF matrix
tfidf = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
tfidf_matrix = tfidf.fit_transform(zomato_df['combined_features'].fillna(''))

# Calculate cosine similarity
nn_model = NearestNeighbors(n_neighbors=11, metric='cosine')
nn_model.fit(tfidf_matrix)

# Create index mapping
indices = pd.Series(zomato_df.index, index=zomato_df['name'].str.lower()).drop_duplicates()


def recommend(name, preferred_price=None, min_rating=None):
    name = name.lower()
    if name not in indices:
        return pd.DataFrame([["Not Found", "-", "-", "-"]], columns=['Restaurant Name', 'Cuisines', 'Rating (★)', 'Approx Cost'])

    idx = indices[name]
    distances, indices_nn = nn_model.kneighbors(tfidf_matrix[idx], n_neighbors=11)
    restaurant_indices = indices_nn.flatten()[1:]  # skip the first (itself)

    recommendations = zomato_df.iloc[restaurant_indices].copy()

    # Apply filters
    if preferred_price:
        recommendations = recommendations[recommendations['price_range'] == preferred_price]
    if min_rating:
        recommendations = recommendations[recommendations['rate'] >= float(min_rating)]

    recommendations = recommendations.drop_duplicates(subset='name')
    recommendations = recommendations.head(10)

    recommendations = recommendations[['name', 'cuisines', 'rate', 'cost']]
    recommendations.reset_index(drop=True, inplace=True)
    recommendations.index += 1
    recommendations['rate'] = recommendations['rate'].round(1)
    recommendations['cost'] = recommendations['cost'].astype(int).astype(str) + " ₹"
    recommendations.columns = ['Restaurant Name', 'Cuisines', 'Rating (★)', 'Approx Cost']

    return recommendations


@app.route('/')
def home():
    return render_template('index.html')  # The initial landing page

@app.route('/web')
def input_page():
    return render_template('web.html')  # The form page


@app.route('/Keywords', methods=['POST'])
def keywords():
    restaurant_name = request.form['restaurant']
    preferred_price = request.form.get('price', '')
    min_rating = request.form.get('rating', '')

    result_df = recommend(restaurant_name, preferred_price, min_rating)

    # Convert to HTML table for rendering
    result_html = result_df.to_html(classes='table table-striped', index=False)

    return render_template('web.html', name=restaurant_name, tables=result_html)


if __name__ == '__main__':
    app.run(debug=True)

