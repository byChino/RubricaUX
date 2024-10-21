const themeToggle = document.getElementById('theme-toggle');
const body = document.body;

// Agregar el evento de cambio de tema al botón
themeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');

    // Cambiar el texto y el ícono del botón al cambiar el tema
    const icon = themeToggle.querySelector('i');
    if (body.classList.contains('dark-mode')) {
        themeToggle.innerHTML = '<i class="fa-regular fa-sun"></i> Modo Claro';
    } else {
        themeToggle.innerHTML = '<i class="fa-regular fa-moon"></i> Modo Oscuro';
    }
});
