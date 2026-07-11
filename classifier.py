import re
from rapidfuzz import fuzz


class ComplexityClassifier:

    def __init__(self):

        self.simple_keywords = [
            "what","who","when","where","define","meaning",
            "translate","capital"
        ]

        self.medium_keywords = [
            "explain","compare","difference",
            "advantages","workflow","summarize"
        ]

        self.complex_keywords = [
            "implement","build","design",
            "optimize","debug","architecture",
            "algorithm","transformer",
            "pytorch","agent","rag"
        ]

    def fuzzy_match(self, query, keyword):

        words = query.split()

        for word in words:

            if fuzz.ratio(word, keyword) > 80:

                return True

        return False

    def predict(self, query):

        query = query.lower()

        score = 10

        for word in self.simple_keywords:

            if self.fuzzy_match(query, word):

                score -= 10

        for word in self.medium_keywords:

            if self.fuzzy_match(query, word):

                score += 20

        for word in self.complex_keywords:

            if self.fuzzy_match(query, word):

                score += 35

        if "code" in query:

            score += 25

        if "python" in query:

            score += 20

        if "java" in query:

            score += 20

        if "c++" in query:

            score += 20

        score = max(0, min(score,100))

        if score < 30:

            label = "simple"

        elif score < 70:

            label = "medium"

        else:

            label = "complex"

        confidence = round(abs(score-50)/50,2)

        return {

            "complexity":score,

            "label":label,

            "confidence":confidence

        }


if __name__=="__main__":

    classifier=ComplexityClassifier()

    while True:

        query=input("Enter Query : ")

        print(classifier.predict(query))