import time

from classifier import ComplexityClassifier
from router import Router
from model_manager import ModelManager
from evaluator import Evaluator
from logger import Logger
from config import FIREWORKS_API_KEY, FIREWORKS_MODEL

classifier = ComplexityClassifier()
router = Router()
manager = ModelManager()
evaluator = Evaluator()
logger = Logger()

while True:

    query = input("\nEnter Query (type 'exit' to quit): ")

    if query.lower() == "exit":
        print("Exiting Hybrid Router...")
        break

    # Step 1: Classify Query
    prediction = classifier.predict(query)

    # Step 2: Decide which model to use
    routing_result = router.decide(query)
    selected_model = routing_result["selected_model"]

    print(f"\nSelected Model: {selected_model}")

    # Step 3: Generate Response + Measure Latency
    start = time.time()

    response = manager.generate(selected_model, query)

    latency = round(time.time() - start, 2)

    # Step 4: Evaluate Response
    evaluation = evaluator.evaluate(query, response)

    # Step 5: Save Log
    logger.log(
        query=query,
        selected_model=selected_model,
        complexity=prediction["complexity"],
        confidence=prediction["confidence"],
        latency=latency,
        evaluation=evaluation,
        fallback=False
    )

    print("API Key Loaded:", FIREWORKS_API_KEY[:10] + "...")
    print("Model:", FIREWORKS_MODEL)

    print(f"\nLatency: {latency} seconds")

    # Step 6: Display Results
    print("\nResponse:")
    print(response)

    print("\nEvaluation:")
    print(evaluation)