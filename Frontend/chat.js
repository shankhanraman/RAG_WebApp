document.getElementById('chat-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const input = document.getElementById('chat-input');
    const message = input.value.trim();
    if (message) {
        displayMessage('You', message);
        input.value = '';
        // Send the message to the backend API and get a response
        fetch('http://127.0.0.1:5000/api/query', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            displayMessage('AI', data.response);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});

function displayMessage(sender, message) {
    const chatContainer = document.getElementById('chat-container');
    const messageElement = document.createElement('div');
    messageElement.innerHTML = `<strong>${sender}:</strong> ${message}`;
    chatContainer.appendChild(messageElement);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}