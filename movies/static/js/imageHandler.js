// Image error handler
function handleImageError(imageElement) {
    imageElement.onerror = null;
    imageElement.src = '{% static "media/image404.png" %}';
    imageElement.classList.add('fallback-image');
}