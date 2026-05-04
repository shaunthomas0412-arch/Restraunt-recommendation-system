# Restaurant_recommender project


A Flask-based web application that helps users discover personalized restaurant recommendations based on cuisine, cost, user preferences, and similarity to their favorite restaurants.

---

## 🚀 Features

- Personalized restaurant suggestions using a content-based recommendation model (TF-IDF + Nearest Neighbors).
- Optional filtering by:
  - Cost range (Budget, Moderate, Expensive, Luxury)
  - Minimum rating
- Interactive frontend built with HTML, CSS, and JavaScript.
- Lightweight and optimized for memory efficiency.

---

## 📁 Project Structure

```
CDC project/
├── Code/
│   ├── app1.py
│   ├── zomato.csv
│   ├── restaurant1.csv                            
│   ├── restaurant1_cleaned.csv        
│   ├── CONTENT_BASE_RECOMMENDER_SYSTEM.ipynb
│   ├── Data_Collection_Preprocessing.ipynb
│   ├── templates/                     
│   │   ├── index.html                 
│   │   └── web.html                   
│   ├── static/                        
│   │   ├── main.css                 
│   │   ├── main.js                    
│   │   └── restaurant.jpg            
```


---

## 🛠️ Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the App
```bash
python app1.py
```

## 📊 Data Source
The dataset (restaurant1_cleaned.csv) was cleaned and preprocessed from Zomato’s public restaurant listings in Bangalore.

Features include: name, cuisines, dish_liked, rate, cost, price_range, and rating_bucket.

## 📌 Dependencies
See requirements.txt for all Python packages used.


---


