// Image error handler
function handleImageError(imageElement) {
    imageElement.onerror = null;
    imageElement.src = document.body.getAttribute('data-fallback-image');
    imageElement.classList.add('fallback-image');
}
