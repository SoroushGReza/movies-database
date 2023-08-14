// Display recent searches
function displayRecentSearches() {
    var recentSearches = sessionStorage.getItem('recent_searches') || "[]";
    recentSearches = JSON.parse(recentSearches);
    var dropdownMenu = document.getElementById('recent-searches');
    dropdownMenu.innerHTML = "";

    // Add recent searches to dropdown
    recentSearches.forEach(function (searchQuery) {
        var searchItem = document.createElement('a');
        searchItem.className = 'dropdown-item';
        searchItem.href = `/movies/search_movies?query=${searchQuery}`;
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
}

// Clear recent searches
function clearRecentSearches(event) {
    event.preventDefault();
    sessionStorage.removeItem('recent_searches');
    displayRecentSearches();

    // Add later: 
    // Send request to server to clear recent searches
}

// Event listener to handle recent searches
document.getElementById('search-input').addEventListener('focus', displayRecentSearches);

displayRecentSearches();
