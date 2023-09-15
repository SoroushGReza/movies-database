// Initialise EmailJS with user ID
(function(){
    emailjs.init("9HmLA-YG0nrtPgthk");
})();

document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault();

    // Get form data
    var from_name = document.getElementById('name').value;
    var from_email = document.getElementById('email').value;
    var message = document.getElementById('message').value;

    // Send the form via EmailJS
    emailjs.send('service_hry28h6', 'template_doij8ju', {
        from_name: from_name,
        from_email: from_email,
        message: message,
    })
    .then(function() {
        // Alert the user that the message has been sent
        alert('Message sent!');
    }, function(error) {
        // Alert the user in case of an error
        alert('Sorry... ' + JSON.stringify(error));
    });
});
