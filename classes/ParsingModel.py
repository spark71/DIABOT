from abc import ABC, abstractmethod

class ParsingModel(ABC):
    def __init__(self, model_name):
        self.model_name = model_name

    @abstractmethod
    def parse_document(self, file_path):
        pass

