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

// Rating stars presented as users rating in review
document.addEventListener('DOMContentLoaded', function() {
    const reviewItems = document.querySelectorAll('.review-item');
    reviewItems.forEach(item => {
        const ratingStars = item.querySelector('.star-rating');
        const rating = parseInt(ratingStars.getAttribute('data-rating'));

        // Fill stars based on user rating
        for (let i = 1; i <= rating; i++) {
            ratingStars.querySelector(`.star${i}`).classList.add('filled');
        }

    });
});
