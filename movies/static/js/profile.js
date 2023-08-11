document.getElementById('edit-profile-button').addEventListener('click', function() {
    var formDiv = this.nextElementSibling;
    if (formDiv.style.display === 'none') {
        formDiv.style.display = 'block';
    } else {
        formDiv.style.display = 'none';
    }
});
