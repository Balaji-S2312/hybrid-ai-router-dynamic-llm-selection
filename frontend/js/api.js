// frontend/js/api.js

const API_URL = "https://hybrid-ai-router-dynamic-llm-selection.onrender.com/chat";

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

        return {
            response: data.response,
            selected_model: data.selected_model,
            latency: data.latency,
            evaluation: data.evaluation,
            token_used: data.token_used,
            token_limit: data.token_limit
        };

    } catch (error) {
        console.error("API Error:", error);
        throw error;
    }
}