/**
 * Practica POO
 * 
 */
/**
 * Cargar recursos
 * 
 */

 var canvas = document.getElementById("canvas");
 var ctx = canvas.getContext("2d");

/**
 * Volores iniciales
 * 
 */

var centro={x:100, y:100};
var radio=50;
var velocidad={x:5, y:2}
animar();

/**
 * Dibujar mundo
 * 
 */

function dibujar() {
    ctx.linewidth=3;
    ctx.strokeStyle="blue"
    ctx.clearRect(0, 0, canvas.width, canvas.height);  
    ctx.beginPath();
    ctx.arc(centro.x,centro.y, radio, 0,2 * Math.PI);
    ctx.stroke();  
    const context = canvas.getContext('2d');
    
}



/**
 * calcular valores
 * 
 */
function calcular() {
    centro.x += velocidad.x;
    centro.y += velocidad.y;
    if (centro.x + radio> canvas.width || centro.x <= radio) {
        velocidad.x*=-1;
    }
    if (centro.y + radio> canvas.height || centro.y <= radio) {
        velocidad.y*=-1;
    }
    
    
}

/**
 * ciclo de animacion 
 * 
 */
function animar() {
    dibujar();
    calcular();
    requestAnimationFrame(animar);
    
}

