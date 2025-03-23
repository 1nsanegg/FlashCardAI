from flashcard_generater import result  # Import AI-generated flashcards
from flashcard_model import Flashcard
from flashcard_trainer import FlashcardTrainer

# Convert AI-generated data into Flashcard objects
flashcard_bank = []
for card in result.split("\n"):  # Assuming AI output is formatted properly
    parts = card.split(": ")
    if len(parts) == 3:  # Ensure it's a complete flashcard
        word, definition, example = parts
        new_flashcard = Flashcard(word, definition, example)
        flashcard_bank.append(new_flashcard)

# Initialize FlashcardTrainer
trainer = FlashcardTrainer(flashcard_bank)
while trainer.still_has_cards():
    trainer.next_card()

print("You've reviewed all the words!")
