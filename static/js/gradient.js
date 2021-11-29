const gradient = document.querySelector(".gradient");

function onMouseMove(event) {
  gradient.style.backgroundImage = 'radial-gradient(at ' + event.clientX + 'px ' + event.clientY + 'px, rgba(144, 137, 141,.3) 0, #72021a 70%)';
}
document.addEventListener("mousemove", onMouseMove);