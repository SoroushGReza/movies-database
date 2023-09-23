// Fix for JSHint warnings
/* jshint esversion: 6 */

// Rating stars in Review form
document.addEventListener("DOMContentLoaded", function() {
    // Get all stars
    const stars = document.querySelectorAll('.rating-star');

    // Add click event listener to each star
    stars.forEach(function(star) {
        star.addEventListener('click', function() {
            // Log when a star is clicked
            console.log("Star clicked: ", this.value);
        });
    });
});

// Show full review 
document.addEventListener("DOMContentLoaded", function() {
    const reviewLinks = document.querySelectorAll('.show-full-review');

    reviewLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const reviewTextElement = e.target.parentElement;
            const fullText = reviewTextElement.getAttribute('data-full-text');
            reviewTextElement.innerHTML = fullText;
        });
    });
});

// Toggle to show / hide all reviews
document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('toggle-reviews');
    if (toggleButton) {
        toggleButton.addEventListener('click', function() {
            const hiddenReviews = document.querySelectorAll('.hidden-review');
            hiddenReviews.forEach(review => {
                review.classList.toggle('show-review');
            });
            toggleButton.textContent = toggleButton.textContent === 'Show all reviews' ? 'Hide Reviews' : 'Show All Reviews';
        });
    }
});

