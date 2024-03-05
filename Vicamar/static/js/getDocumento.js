document.getElementById("descargar").addEventListener("click", function () {
    const nombre = document.getElementById("nombre").textContent;
    const dni = document.getElementById("dni").textContent;
    const ruc = document.getElementById("ruc").textContent;
    const url = "http://127.0.0.1:8000/Vicamar/getCotizacion/";
    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type" : "application/json"
        },
        body: JSON.stringify({
            "NOMBRE" : nombre,
            "DNI":dni,
            "RUC": ruc
        })
    }).then(response => {
        return response.json();
    }).then(data => {
        console.log(data)
    })
})