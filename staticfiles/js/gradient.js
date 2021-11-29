const gradient = document.querySelector(".gradient");

function onMouseMove(event) {
  gradient.style.backgroundImage = 'radial-gradient(at ' + event.clientX + 'px ' + event.clientY + 'px, rgba(164, 162, 163,.3) 0, #90898d 70%)';
}
document.addEventListener("mousemove", onMouseMove);