import docx2txt

class User:
    def __init__(self, name):
        self.name = name
        self.documents = []

    def add_document(self, document):
        self.documents.append(document)

    def process_documents(self):
        for doc in self.documents:
            if doc.file_path.endswith(".txt"):
                with open(doc.file_path, 'r', encoding='utf-8') as file:
                    doc.text = file.read()
            elif doc.file_path.endswith(".docx"):
                doc.text = docx2txt.process(doc.file_path)
            else:
                raise Exception("Unsupported file format")

