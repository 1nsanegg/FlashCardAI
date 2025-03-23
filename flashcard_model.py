class Flashcard:
    def __init__(self, word, definition, example):
        self.word = word
        self.definition = definition
        self.example = example

    def display(self):
        print(f"Word: {self.word}")
        print(f"Definition: {self.definition}")
        print(f"Example: {self.example}\n")
