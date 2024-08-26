document.getElementById('waitlist-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value.trim();
    if (email) {
        fetch('http://127.0.0.1:5000/waitlist', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: email })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('response-message').textContent = data.message;
        })
        .catch(error => {
            document.getElementById('response-message').textContent = 'An error occurred.';
        });
    }
});
