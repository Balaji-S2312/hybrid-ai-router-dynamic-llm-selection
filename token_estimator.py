import re


class TokenEstimator:

    def estimate(self, text):

        # Approximate token count
        words = re.findall(r"\S+", text)

        estimated_tokens = int(len(words) * 1.3)

        return estimated_tokens

    def estimate_cost(self, prompt):

        input_tokens = self.estimate(prompt)

        if input_tokens < 20:
            expected_output = 100
        elif input_tokens < 50:
            expected_output = 250
        else:
            expected_output = 500

        total = input_tokens + expected_output

        return {
            "input_tokens": input_tokens,
            "expected_output_tokens": expected_output,
            "total_estimated_tokens": total
        }


if __name__ == "__main__":

    estimator = TokenEstimator()

    result = estimator.estimate_cost(
        "Write a Python implementation of a Transformer from scratch."
    )

    print(result)