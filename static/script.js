document.getElementById('send-button').addEventListener('click', sendMessage);
document.getElementById('user-input').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() === '') return;

    displayMessage('user', userInput);
    document.getElementById('user-input').value = '';  // Clear input field

    fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        if (data[0] && data[0].text) {
            displayMessage('bot', data[0].text);
        }
    })
    .catch(error => {
        displayMessage('bot', 'Error: Unable to reach the server.');
        console.error('Error:', error);
    });
}

function displayMessage(sender, message) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    messageDiv.innerHTML = `<strong>${sender === 'user' ? 'You' : 'Bot'}:</strong> ${message}`;
    document.getElementById('messages').appendChild(messageDiv);
    document.getElementById('chat-window').scrollTop = document.getElementById('chat-window').scrollHeight;
}
