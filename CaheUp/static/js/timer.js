let progressBar = document.getElementById("progress-bar");
let timerCircle = document.getElementById("timer-circle");

document.addEventListener("load", function() {
    let timer = 10;
    
    setInterval(function () {
        if (timer>0) {
            progressBar.style.width = ((timer--) / 10) * 100 + "%";
            timerCircle.textContent = timer            
        }
    }, 1000);
}, true);
