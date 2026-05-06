from agents.base_agent import BaseAgent

class BudgetingAgent(BaseAgent):
    name = "BudgetingAgent"

    def run(self, data):
        remaining = data["income"] - data["expenses"]
        return {"monthly_remaining": remaining}
