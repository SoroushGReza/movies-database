document-addEventListener('DOMContentLoaded', function() {
    document.getElementById('edit-profile-button').addEventListener('click', function() {
        var form = document.getElementById('edit-profile-form');
        form.style.display = form.style.display === 'none' ? 'block' : 'none';
    });
});