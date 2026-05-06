from agents.base_agent import BaseAgent

class RecommendationAgent(BaseAgent):
    name = "RecommendationAgent"

    def run(self, data):
        return {
            "recommendation": "Consider saving at least 20% of your income."
        }
