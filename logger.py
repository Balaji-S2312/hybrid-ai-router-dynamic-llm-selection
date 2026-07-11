import json
from datetime import datetime


class Logger:

    def __init__(self, log_file="logs.jsonl"):
        self.log_file = log_file

    def log(
    self,
    query,
    selected_model,
    complexity,
    confidence,
    latency,
    evaluation,
    fallback=False
):

        log_entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "query": query,
            "selected_model": selected_model,
            "complexity": complexity,
            "confidence": confidence,
            "latency": latency,
            "evaluation_score": evaluation["score"],
            "passed": evaluation["passed"],
            "fallback": fallback
        }

        with open(self.log_file, "a") as f:
            f.write(json.dumps(log_entry) + "\n")