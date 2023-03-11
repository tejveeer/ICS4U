
document.addEventListener("click", (e) => {
    const [width, height] = [e.clientX, e.clientY];
    const circle = document.getElementById("circle");

    circle.style.transform = `translate(${width - circle.offsetLeft - 25}px, ${height - circle.offsetTop - 25}px)`;
});

