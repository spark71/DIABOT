from abc import ABC, abstractmethod

class BaseModel(ABC):
    def __init__(self, model_name):
        self.model_name = model_name

    @abstractmethod
    def preprocess_text(self, text):
        pass

    @abstractmethod
    def train_model(self, X, y):
        pass

    @abstractmethod
    def predict(self, text):
        pass

