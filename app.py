import time
from fastapi import FastAPI
from pydantic import BaseModel

from classifier import ComplexityClassifier
from router import Router
from model_manager import ModelManager
from evaluator import Evaluator
from logger import Logger

classifier = ComplexityClassifier()
router = Router()
manager = ModelManager()
evaluator = Evaluator()
logger = Logger()

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Hybrid AI Router is running!"}

@app.post("/chat")
def chat(request: QueryRequest):
    query = request.query

    prediction = classifier.predict(query)
    routing_result = router.decide(query)
    selected_model = routing_result["selected_model"]

    start = time.time()
    response = manager.generate(selected_model, query)
    latency = round(time.time() - start, 2)

    evaluation = evaluator.evaluate(query, response)

    logger.log(
        query=query,
        selected_model=selected_model,
        complexity=prediction["complexity"],
        confidence=prediction["confidence"],
        latency=latency,
        evaluation=evaluation,
        fallback=False,
    )

    return {
    "response": response,
    "selected_model": selected_model,
    "latency": latency,
    "evaluation": evaluation,
    "token_used": len(query.split()) + len(response.split()),
    "token_limit": 32768
}