// Wait for DOM to fully load before running script
document.addEventListener('DOMContentLoaded', (event) => {
    
    // Loop through each review item in page
    document.querySelectorAll('.review-item-my-reviews').forEach(function(reviewItem) {
        
        // Get unique ID of current review
        const reviewId = reviewItem.querySelector('button[data-review-id]').getAttribute('data-review-id');
        
        // Add an event listener to the Edit button in current review
        reviewItem.querySelector('#edit-button-' + reviewId).addEventListener('click', function() {
            
            // Hide Edit button
            reviewItem.querySelector('#edit-button-' + reviewId).style.display = 'none';
            
            // Show Save button
            reviewItem.querySelector('#save-button-' + reviewId).style.display = 'block';
            
            // Hide static review text
            reviewItem.querySelector('.review-text').style.display = 'none';
            
            // Show textarea with the current review text
            reviewItem.querySelector('#review-textarea-' + reviewId).style.display = 'block';
        });
    });
});

// Wait for DOM to fully load before runing script
document.addEventListener('DOMContentLoaded', (event) => {
    
    // Loop through each review item in the page
    document.querySelectorAll('.review-item-my-reviews').forEach(function(reviewItem) {
        
        // Get the unique ID of current review
        const reviewId = reviewItem.querySelector('button[data-review-id]').getAttribute('data-review-id');
        
        // Add an event listener to the Save button of current review
        reviewItem.querySelector('#save-button-' + reviewId).addEventListener('click', function() {
            
            // Get the new text from textarea
            const newText = reviewItem.querySelector('#review-textarea-' + reviewId).value;
            
            // Update the static review text with the new text
            reviewItem.querySelector('.review-text').textContent = newText;
            
            // Hide Save button
            reviewItem.querySelector('#save-button-' + reviewId).style.display = 'none';
            
            // Show Edit button
            reviewItem.querySelector('#edit-button-' + reviewId).style.display = 'block';
            
            // Hide textarea
            reviewItem.querySelector('#review-textarea-' + reviewId).style.display = 'none';
            
            // Show updated static review text
            reviewItem.querySelector('.review-text').style.display = 'block';
        });
    });
});
