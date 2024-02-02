from abc import ABC, abstractmethod
import spacy


class NerModel(ABC):
    def __init__(self, model_name):
        self.model_name = model_name

    @abstractmethod
    def extract_entities(self, text):
        pass

class SpacyNerModel(NerModel):
    def extract_entities(self, text):
        # Пример реализации метода extract_entities
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        entities = [(entity.text, entity.label_) for entity in doc.ents]
        return entities

