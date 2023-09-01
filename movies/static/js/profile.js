document.addEventListener('DOMContentLoaded', function () {
    var editProfileButton = document.getElementById('edit-profile-button');
    if (editProfileButton) { // Check if the element exists
        editProfileButton.addEventListener('click', function () {
            var form = document.getElementById('edit-profile-form');
            form.style.display = form.style.display === 'none' ? 'block' : 'none';
        });
    } else {
        console.warn('Edit profile button not found'); // Warning if element is not found
    }
});

// Detele user reviews confirmation
document.addEventListener("DOMContentLoaded", function () {
    const deleteButtons = document.querySelectorAll('.btn-danger');
    deleteButtons.forEach(function (button) {
        button.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent default
            const confirmation = window.confirm('Are you sure you want to delete this review?');
            if (confirmation) {
                const reviewId = event.target.getAttribute('data-review-id');
                const url = `/movies/delete_review/${reviewId}/`;
                fetch(url, {
                        method: 'POST',
                        headers: {
                            'X-Requested-With': 'XMLHttpRequest',
                            'X-CSRFToken': csrftoken
                        },
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.status === 'success') {
                            event.target.closest('.review-item').remove();
                        }
                    });
                // Perform delete operation
                console.log('User confirmed deletion');
            } else {
                console.log('User canceled deletion');
            }
        });
    });
});