/* jshint esversion: 6 */
'use strict';

// Check window size and apply changes according to size
function checkWindowSize() {
    // Get element with id "navbarDropdown"
    const linkElement = document.getElementById("navbarDropdown");

    // Get custom icon for toggler button
    const customTogglerIcon = document.getElementById("custom-toggler-icon");

    // Define media query for screen width between 768px and 991px
    const mediaQuery = window.matchMedia("(min-width: 768px) and (max-width: 991px)");

    // Check if media query matches
    if (mediaQuery.matches) {
        // Set the text of the link element to "Movie Base"
        linkElement.textContent = "Movie Base";

        // Add class "movie-base-style" to style in CSS
        linkElement.classList.add("movie-base-style");

        // Set text of the custom toggler icon to "Movie Base"
        customTogglerIcon.textContent = "Movie Base";

        // Add class "movie-base-style" to style it in CSS
        customTogglerIcon.classList.add("movie-base-style");
    } else {
        // Set the text of the link element to "Profile"
        linkElement.textContent = "Profile";

        // Remove the class "movie-base-style"
        linkElement.classList.remove("movie-base-style");

        // Set the text of the custom toggler icon to "Movie Base"
        customTogglerIcon.textContent = "Movie Base";

        // Remove the class "movie-base-style"
        customTogglerIcon.classList.remove("movie-base-style");
    }
}

// Run the checkWindowSize function when the page loads
window.addEventListener("load", checkWindowSize);

// Run the checkWindowSize function whenever the window size changes
window.addEventListener("resize", checkWindowSize);
