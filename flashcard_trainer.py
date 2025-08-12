# This class works as a controller, take flashcards and display it

class FlashcardTrainer:
    def __init__(self, flashcards):
        self.flashcards = flashcards
        self.index = 0

    def next_card(self):
        if self.index < len(self.flashcards):
            card = self.flashcards[self.index]
            card.display()
            self.index += 1
        else:
            print("You've reviewed all the words!")

    def still_has_cards(self):
        return self.index < len(self.flashcards)
