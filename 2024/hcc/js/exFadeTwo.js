document.addEventListener('DOMContentLoaded', () => {
    const image = document.getElementById('fadeImage');
    const images = ['image1.jpg', 'image2.jpg'];
    let currentIndex = 0;

    image.addEventListener('click', () => {
        image.classList.add('fade-out');

        setTimeout(() => {
            currentIndex = (currentIndex + 1) % images.length;
            image.src = images[currentIndex];
            image.classList.remove('fade-out');
        }, 1000); // Wait for the fade-out transition to complete
    });
});

