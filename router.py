from classifier import ComplexityClassifier
from config import (
    LOCAL_THRESHOLD,
    REMOTE_THRESHOLD,
    CONFIDENCE_THRESHOLD
)

class Router:

    def __init__(self):

        self.classifier = ComplexityClassifier()

    def decide(self, query):

        result = self.classifier.predict(query)

        score = result["complexity"]

        confidence = result["confidence"]

        # Decision Rules

        if score < LOCAL_THRESHOLD:

            model = "local"

        elif score < REMOTE_THRESHOLD:

            if confidence > CONFIDENCE_THRESHOLD:
                model = "local"
            else:
                model = "fireworks"

        else:

            model = "fireworks"

        return {

            "selected_model": model,

            "complexity": score,

            "confidence": confidence,

            "label": result["label"]

        }


if __name__ == "__main__":

    router = Router()

    while True:

        query = input("Query : ")

        decision = router.decide(query)

        print(decision)