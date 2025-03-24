
const container=document.querySelector(".container");

// document.addEventListener("mousemove", (event) => {
//     const x = event.clientX;
//     const y = event.clientY;
//     if(x >960){
//         seguidor.style.borderRadius=0
//     }else{
//         seguidor.style.borderRadius="50%"
//     }
//     seguidor.style.transform = `translate(${x}px, ${y}px)`;
// });
function gotasAguas(min, max) {
    let gotas = Math.floor(Math.random() * (max - min + 1) + min);
    
    for (let i = 0; i < gotas; i++) {
        let gota = document.createElement("div");
        gota.classList.add("gotas");

        // Calcular la posición horizontal aleatoria
        let width = Math.random() * container.clientWidth;
        gota.style.left = `${width}px`;

        // Añadir la gota al contenedor
        container.appendChild(gota);

        // Animar la gota para que se mueva hacia abajo
        setTimeout(() => {
            gota.style.transition = "top 2s linear";
            gota.style.top = "100%";
        }, 10);

        // Eliminar la gota después de que haya caído
        setTimeout(() => {
            gota.remove();
        }, 2000); // 2000ms = 2 segundos (igual al tiempo de la animación)
    }
}

// Llamar a la función cada 5 segundos
setInterval(() => {
    gotasAguas(10, 25);
}, 5000);

