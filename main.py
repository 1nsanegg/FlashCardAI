# main.py
from flashcard_generater import get_flashcards
from flashcard_model import Flashcard
from flashcard_trainer import FlashcardTrainer


isStop = False
while not isStop:
    raw_data = get_flashcards()
    # Parse the AI output into Flashcard objects
    flashcard_bank = []
    for block in raw_data.strip().split("---"):
        lines = [line.strip() for line in block.strip().split("\n") if line.strip()]
        if len(lines) == 3 and all(line.startswith(("Word:", "Definition:", "Example:")) for line in lines):
            word = lines[0].split(":", 1)[1].strip()
            definition = lines[1].split(":", 1)[1].strip()
            example = lines[2].split(":", 1)[1].strip()
            flashcard_bank.append(Flashcard(word, definition, example))

    # Train flashcards
    trainer = FlashcardTrainer(flashcard_bank)
    while trainer.still_has_cards():
        trainer.next_card()

    user_input = input("Do you wish to continue? (y/n)")
    if user_input == "n":
        isStop = True


print("✅ You've reviewed all the words!")
