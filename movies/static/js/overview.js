//     Rating stars in Review form
document.addEventListener("DOMContentLoaded", function() {
    // Get all stars
    const stars = document.querySelectorAll('.rating-star');
    
    // Add click event listener to each star
    stars.forEach(function(star) {
        star.addEventListener('click', function() {
            // Log when a star is clicked
            console.log("Star clicked: ", this.value);

            // Get the rating value
            const ratingValue = this.value;
            
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
