from fastapi import FastAPI, Depends
from backend.database import Base, engine
from agents.budgeting_agent import BudgetingAgent
from agents.risk_agent import RiskAgent
from agents.recommendation_agent import RecommendationAgent

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Secure Multi-Agent Budget Advisor")

budget_agent = BudgetingAgent()
risk_agent = RiskAgent()
rec_agent = RecommendationAgent()

@app.post("/analyze")
def analyze_budget(data: dict):
    result = {}
    result.update(budget_agent.run(data))
    result.update(risk_agent.run(data))
    result.update(rec_agent.run(data))
    return result
