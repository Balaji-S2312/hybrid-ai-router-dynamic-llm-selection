const steps = document.querySelectorAll(".step");

// Reset all routing steps
function resetSteps() {

    steps.forEach(step => {
        step.classList.remove("active");
    });

}

// Highlight a specific step
function activateStep(index) {

    if (index >= 0 && index < steps.length) {
        steps[index].classList.add("active");
    }

}

// Animate routing flow
async function animateRouting() {

    resetSteps();

    for (let i = 0; i < steps.length; i++) {

        activateStep(i);

        await new Promise(resolve => setTimeout(resolve, 500));

    }

}

// Card animation
function animateCards() {

    const cards = document.querySelectorAll(".card-box");

    cards.forEach((card, index) => {

        card.style.opacity = "0";
        card.style.transform = "translateY(20px)";

        setTimeout(() => {

            card.style.transition = "0.4s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0px)";

        }, index * 100);

    });

}

// Success pulse
function successAnimation() {

    const status = document.getElementById("status");

    status.classList.add("success-glow");

    setTimeout(() => {

        status.classList.remove("success-glow");

    }, 1200);

}

// Loading animation
function showLoading() {

    document.getElementById("response").innerHTML = `

        <div class="loading">

            <span></span>
            <span></span>
            <span></span>

        </div>

    `;

}