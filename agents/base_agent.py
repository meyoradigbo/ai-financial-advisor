class BaseAgent:
    name = "BaseAgent"

    def run(self, data: dict) -> dict:
        raise NotImplementedError
