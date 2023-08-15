document.addEventListener('DOMContentLoaded', function() {
    var editProfileButton = document.getElementById('edit-profile-button');
    if (editProfileButton) { // Check if the element exists
        editProfileButton.addEventListener('click', function() {
            var form = document.getElementById('edit-profile-form');
            form.style.display = form.style.display === 'none' ? 'block' : 'none';
        });
    } else {
        console.warn('Edit profile button not found'); // Warning if element is not found
    }
});
