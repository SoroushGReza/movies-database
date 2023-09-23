// Fix for JsHint validation
/* jshint esversion: 6 */


// Get CSRF token from cookies 
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');


// Edit Profile Button
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
    const deleteButtons = document.querySelectorAll('.delete-my-review');
    deleteButtons.forEach(function (button) {
        button.addEventListener('click', function (event) {
            event.preventDefault(); // Prevent default
            const confirmation = window.confirm('Are you sure you want to delete this review?');
            if (confirmation) {
                const reviewId = event.currentTarget.getAttribute('data-review-id');
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
                            event.target.closest('.review-item-my-reviews').remove();
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