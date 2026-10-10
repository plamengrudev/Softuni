const slides = document.querySelectorAll(".slide");
const previousButton = document.querySelector("#previous-slide");
const nextButton = document.querySelector("#next-slide");

let currentSlide = 0;

function showSlide(index) {
    if (!slides.length) {
        return;
    }

    currentSlide = (index + slides.length) % slides.length;

    slides.forEach((slide, slideIndex) => {
        slide.classList.toggle(
            "is-active",
            slideIndex === currentSlide,
        );
    });
}

previousButton?.addEventListener("click", () => {
    showSlide(currentSlide - 1);
});

nextButton?.addEventListener("click", () => {
    showSlide(currentSlide + 1);
});

document.addEventListener("keydown", (event) => {
    if (event.key === "ArrowLeft") {
        showSlide(currentSlide - 1);
    }

    if (event.key === "ArrowRight") {
        showSlide(currentSlide + 1);
    }
});