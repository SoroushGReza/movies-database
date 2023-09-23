/* global $ */

// Wait until document is fully loaded
$(document).ready(function() {
    // Attach event handler to elements with class 'review-form'
    $('.review-form').on('submit', function(e) {
        e.preventDefault();

        // Make an AJAX POST request to subbmit form data
        $.ajax({
            type: "POST",
            // Get URL from the form action
            url: $(this).attr('action'),
            // Prepare form data for the AJAX request
            data: $(this).serialize(),
            success: function(response) {
                if (response.status === "success") {
                    // Close the modal containing the form
                    $('.modal').modal('hide');
                    // Display the success message to user
                    $('#ajax-success-message').show();
                } else {
                    // If server respons with an error, log the error details in the console
                    console.error('Form errors:', response.errors);
                }
            },
            error: function(error) {
                // If AJAX request fails, log the server error in the console
                console.error('Server error:', error);
            }
        });
    });
});
