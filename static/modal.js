
function showModal() {
    const modal = document.getElementById("login-modal");
    modal.style.display = "block";

}

function closeModal() {
    const modal = document.getElementById("login-modal");
    modal.style.display = "none";
}

setTimeout(function () {
    let messages = document.getElementById('message-timeout');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3500);

