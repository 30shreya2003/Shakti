let index = 0;
const slides = document.querySelectorAll(".carousel-slide");

function showSlide() {
    slides.forEach((slide, i) => {
        slide.style.display = (i === index) ? "block" : "none";
    });
    index = (index + 1) % slides.length;
}

setInterval(showSlide, 4000);
showSlide();

document.querySelectorAll(".nav-links a").forEach(anchor => {
    anchor.addEventListener("click", function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute("href")).scrollIntoView({
            behavior: "smooth"
        });
    });
});
