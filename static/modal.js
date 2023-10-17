
/**
 * Function to display the login modal 
 * by setting its style property to "block"
 */
function showModal() {
    const modal = document.getElementById("login-modal");
    modal.style.display = "block";

}

/**
 * Function to hide the login modal 
 * by setting its style property to "none"
 */
function closeModal() {
    const modal = document.getElementById("login-modal");
    modal.style.display = "none";
}

/**
 * Set timeout for 5 seconds
 * to automatically close a bootstrap alert message
 */
setTimeout(function () {
    let messages = document.getElementById('message-timeout');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 5000);

