// Display recent searches
function displayRecentSearches() {
    fetch('/movies/get_recent_searches/')
        .then(response => response.json())
        .then(data => {
            var recentSearches = data.recent_searches;
            var dropdownMenu = document.getElementById('recent-searches');
            dropdownMenu.innerHTML = "";

            // Add recent searches to dropdown
            recentSearches.forEach(function (searchQuery) {
                var searchItem = document.createElement('a');
                searchItem.className = 'dropdown-item';
                searchItem.href = `/movies/search/?query=${searchQuery}`;
                searchItem.textContent = searchQuery;
                dropdownMenu.appendChild(searchItem);
            });

            // Add clear link if there is recent searches
            if (recentSearches.length > 0) {
                var clearLink = document.createElement('a');
                clearLink.className = 'dropdown-item clear-link';
                clearLink.href = '#';
                clearLink.textContent = 'Clear';
                clearLink.onclick = clearRecentSearches;
                dropdownMenu.appendChild(clearLink);
            }
        });
}


// Clear recent searches
function clearRecentSearches(event) {
    event.preventDefault();
    // Send request to server to clear recent searches
    fetch('/movies/clear_search_history/')
        .then(response => response.json())
        .then(data => {
            if (data.status === 'success') {
                sessionStorage.removeItem('recent_searches');
                displayRecentSearches();
            }
        });
    }

// Call the displayRecentSearches function when page loads
window.onload = function() {
    displayRecentSearches();
}
