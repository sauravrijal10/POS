// static/src/js/create_user.js
document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('createUserForm');
    if (form) {
        form.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission

            const username = document.getElementById('username').value;

            fetch('/create_user', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username: username }),
            })
            .then(response => response.text())
            .then(data => {
                document.open();
                document.write(data);
                document.close();
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }
});
