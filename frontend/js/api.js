// frontend/js/api.js

const API_URL = "http://127.0.0.1:8000/generate";

/**
 * Send query to FastAPI backend
 * @param {string} query
 * @returns {Promise<Object>}
 */
async function generateResponse(query) {
    try {
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                query: query
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const data = await response.json();

        return data;

    } catch (error) {
        console.error("API Error:", error);

        return {
            response: "Unable to connect to FastAPI server.",
            selected_model: "-",
            complexity: "-",
            confidence: "-",
            latency: "-",
            evaluation: {
                score: 0,
                passed: false
            },
            tokens_used: 0,
            tokens_remaining: 0
        };
    }
}