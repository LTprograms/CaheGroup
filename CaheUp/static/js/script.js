
function mostrarModal() {
    var modal = document.getElementById("myModal");
    modal.style.display = "block";
    console.log("sfdadf")
}

function cerrarModal() {
    var modal = document.getElementById("myModal");
    modal.style.display = "none";
}

document.getElementById("cerrarModal").addEventListener("click", function () {
    cerrarModal()
})
document.getElementById("comenzarYa").addEventListener("click", function () {
    cerrarModal()
})

document.addEventListener("load", function() {
    mostrarModal();
}, true);


