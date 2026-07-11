// DOM Elements
const queryInput = document.getElementById("query");
const generateBtn = document.getElementById("generateBtn");

const responseBox = document.getElementById("response");

const modelBox = document.getElementById("model");
const complexityBox = document.getElementById("complexity");
const confidenceBox = document.getElementById("confidence");
const latencyBox = document.getElementById("latency");
const statusBox = document.getElementById("status");
const tokensUsedBox = document.getElementById("tokensUsed");
const tokensRemainingBox = document.getElementById("tokensRemaining");
const scoreBox = document.getElementById("score");
// Generate Button Click
generateBtn.addEventListener("click", async () => {

    const query = queryInput.value.trim();

    if (!query) {
        alert("Please enter a query.");
        return;
    }

    // Disable button
    generateBtn.disabled = true;
    generateBtn.innerHTML = "Generating...";

    // Remove previous animation
    responseBox.classList.remove("fade-in");

    // Loading Animation
    responseBox.innerHTML = `
        <div class="loading">
            <span></span>
            <span></span>
            <span></span>
        </div>
    `;

    try {

        // Call FastAPI
        const data = await generateResponse(query);

        // Dashboard
        modelBox.textContent = data.selected_model || "--";
        complexityBox.textContent = data.complexity || "--";
        confidenceBox.textContent = data.confidence || "--";
        latencyBox.textContent = `${data.latency} sec`;

        statusBox.textContent =
            data.evaluation && data.evaluation.passed
                ? "Passed ✅"
                : "Failed ❌";
        scoreBox.textContent = data.evaluation?.score ?? "--";
        tokensUsedBox.textContent = data.token_used ?? "--";
        tokensRemainingBox.textContent =
    data.token_limit ? data.token_limit - data.token_used : "--";

        // Response
        responseBox.textContent = data.response || "No response received.";

        // Fade animation
        responseBox.classList.add("fade-in");

    } catch (error) {

        console.error(error);

        responseBox.innerHTML = `
            <span style="color:#ff4d4d;font-weight:bold;">
                Unable to connect to backend.
            </span>
        `;

    } finally {

        generateBtn.disabled = false;
        generateBtn.innerHTML = "Generate";

    }

});