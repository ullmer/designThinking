document.addEventListener('DOMContentLoaded', () => {
    const image = document.getElementById('fadeImage');
    let isFadedOut = false;

    image.addEventListener('click', () => {
        if (isFadedOut) {
            image.classList.remove('fade-out');
            image.classList.add('fade-in');
        } else {
            image.classList.remove('fade-in');
            image.classList.add('fade-out');
        }
        isFadedOut = !isFadedOut;
    });
});

