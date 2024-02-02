import os
from collections import defaultdict

class Corpus:
    def __init__(self, corpus_dir):
        self.corpus_dir = corpus_dir
        self.documents = {}
        self.word_count = defaultdict(int)
        self.build_corpus()

    def build_corpus(self):
        for filename in os.listdir(self.corpus_dir):
            if filename.endswith(".txt"):
                with open(os.path.join(self.corpus_dir, filename), 'r', encoding='utf-8') as file:
                    text = file.read()
                    self.documents[filename] = text
                    for word in text.split():
                        self.word_count[word] += 1

    def get_document(self, doc_name):
        return self.documents.get(doc_name, "Document not found")

    def get_word_count(self, word):
        return self.word_count.get(word, 0)
