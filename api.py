import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from classifier import ComplexityClassifier
from router import Router
from model_manager import ModelManager
from evaluator import Evaluator
from logger import Logger


# -------------------------------------------------
# Initialize FastAPI
# -------------------------------------------------

app = FastAPI(title="Hybrid AI Router API")


# -------------------------------------------------
# Enable CORS
# -------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# -------------------------------------------------
# Initialize Components
# -------------------------------------------------

classifier = ComplexityClassifier()
router = Router()
manager = ModelManager()
evaluator = Evaluator()
logger = Logger()


# -------------------------------------------------
# Request Model
# -------------------------------------------------

class QueryRequest(BaseModel):
    query: str


# -------------------------------------------------
# Health Check
# -------------------------------------------------

@app.get("/")
def root():
    return {"message": "Hybrid AI Router API Running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


# -------------------------------------------------
# Generate Endpoint
# -------------------------------------------------

@app.post("/generate")
def generate(data: QueryRequest):

    query = data.query

    prediction = classifier.predict(query)

    route = router.decide(query)

    selected_model = route["selected_model"]

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
        fallback=False
    )

    return {

        "response": response,

        "selected_model": selected_model,

        "complexity": prediction["complexity"],

        "confidence": prediction["confidence"],

        "latency": latency,

        "evaluation": evaluation,

        "tokens_used": 0,

        "tokens_remaining": 0

    }