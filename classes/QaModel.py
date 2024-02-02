class QaModel:
    def __init__(self, qa_data):
        self.qa_data = qa_data

    def get_answer(self, question):
        if question in self.qa_data:
            return self.qa_data[question]
        else:
            return "Извините, я не могу ответить на ваш вопрос в данный момент."


