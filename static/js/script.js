export function RecommendMovies() {
    let data = document.querySelector('input[name="film"]').value;
    fetch('/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
    .then()
    .then()
    .catch((error) => console.error('Error:', error));
}

// Attach the RecommendMovies function as a click event handler
document.getElementById('recommend-button').addEventListener('click', RecommendMovies);