import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)

class BaseAgent(ABC):
    name = "BaseAgent"

    @abstractmethod
    def run(self, data: dict) -> dict:
        pass

    def log(self, message: str):
        logging.info(f"[{self.name}] {message}")
