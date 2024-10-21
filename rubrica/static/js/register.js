function togglePassword() {
    var passwordInput = document.getElementById('password');
    var eyeIcon = document.getElementById('eye-icon-password');

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeIcon.classList.remove('fa-eye');
        eyeIcon.classList.add('fa-eye-slash'); // Cambia a ojo cerrado
    } else {
        passwordInput.type = "password";
        eyeIcon.classList.remove('fa-eye-slash');
        eyeIcon.classList.add('fa-eye'); // Cambia a ojo abierto
    }
}

function toggleConfirmPassword() {
    var confirmPasswordInput = document.getElementById('confirmPassword');
    var eyeIconConfirm = document.getElementById('eye-icon-confirm');

    if (confirmPasswordInput.type === "password") {
        confirmPasswordInput.type = "text";
        eyeIconConfirm.classList.remove('fa-eye');
        eyeIconConfirm.classList.add('fa-eye-slash'); // Cambia a ojo cerrado
    } else {
        confirmPasswordInput.type = "password";
        eyeIconConfirm.classList.remove('fa-eye-slash');
        eyeIconConfirm.classList.add('fa-eye'); // Cambia a ojo abierto
    }
}
