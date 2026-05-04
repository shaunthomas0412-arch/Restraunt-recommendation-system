document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    const input = document.querySelector('input[name="restaurant"]');
    const loading = document.createElement('div');
    loading.id = "loading";
    loading.innerText = "Fetching recommendations...";
    form.parentNode.insertBefore(loading, form.nextSibling);

    form.addEventListener('submit', function (e) {
        if (input.value.trim() === '') {
            e.preventDefault();
            alert("Please enter a restaurant name.");
        } else {
            loading.style.display = 'block';
        }
    });
});
