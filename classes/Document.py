import docx2txt

class Document:
    def __init__(self, file_path):
        self.file_path = file_path
        self.text = self.extract_text()

    def extract_text(self):
        if self.file_path.endswith(".txt"):
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return file.read()
        elif self.file_path.endswith(".docx"):
            return docx2txt.process(self.file_path)
        else:
            raise Exception("Unsupported file format")

    def get_text(self):
        return self.text

