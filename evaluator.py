class Evaluator:

    def __init__(self):
        pass

    def evaluate(self, query, response):

        score = 100

        if len(response.strip()) < 20:
            score -= 40

        if "I don't know" in response:
            score -= 50

        if "cannot answer" in response.lower():
            score -= 50

        passed = score >= 60

        return {
            "score": score,
            "passed": passed
        }


if __name__ == "__main__":

    evaluator = Evaluator()

    result = evaluator.evaluate(
        "What is AI?",
        "Artificial Intelligence is the field of building intelligent systems."
    )

    print(result)