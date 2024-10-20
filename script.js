document.getElementById('surpriseButton').addEventListener('click', function() {
    const flowerContainer = document.querySelector('.flower-container');
    const mainContainer = document.querySelector('.container');
    const text_flower = document.querySelector('.text-flower');
    const body = document.querySelector('body');

    flowerContainer.style.display = 'block'; // Hiển thị hoa
    mainContainer.style.display = 'none';
    text_flower.style.display = 'block';
    body.style.alignItems = "start"
    const button = document.getElementById('surpriseButton');
    button.textContent = "Bất ngờ đã đến!";
    button.disabled = true;
});
