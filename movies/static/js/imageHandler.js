/* exported handleImageError */
// Image error handler
function handleImageError(imageElement) {
    'use strict';
    imageElement.onerror = null;
    imageElement.src = imageElement.getAttribute('data-fallback-image');
    imageElement.classList.add('fallback-image');
}
