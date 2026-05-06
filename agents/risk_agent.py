from agents.base_agent import BaseAgent

class RiskAgent(BaseAgent):
    name = "RiskAgent"

    def run(self, data):
        if data["expenses"] > data["income"] * 0.7:
            return {"risk": "High spending risk"}
        return {"risk": "Low risk"}
