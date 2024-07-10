// registration.js

document.addEventListener('DOMContentLoaded', function() {
    var form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent form submission

        // Get form input values
        var username = form.querySelector('#id_username').value;
        var password = form.querySelector('#id_password1').value;

        // Store username and password in localStorage
        localStorage.setItem('username', username);
        localStorage.setItem('password', password);

        // Redirect to home page
        window.location.href = '/accounts/home/';
    });
});