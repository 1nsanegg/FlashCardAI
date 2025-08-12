# 🃏 AI Vocabulary Flashcard Trainer

A simple Python-based flashcard application that generates vocabulary cards using a **local GPT-OSS model (via Ollama)**, then lets you review them interactively in your terminal.

## ✨ Features

- **🤖 AI-powered flashcards** — Automatically generates vocabulary with definitions and examples
- **🏠 Local model** — Uses GPT-OSS via Ollama (no external API needed)
- **💬 Interactive training** — Review flashcards one by one in the terminal
- **🧩 Modular structure** — Clean separation of model, trainer, and generator logic
- **📚 Customizable content** — Generate flashcards for any topic or difficulty level

## 📂 Project Structure

```
flashcard-trainer/
├── flashcard_model.py      # Defines the Flashcard class
├── flashcard_trainer.py    # Manages reviewing and displaying flashcards
├── flashcard_generator.py  # Gets flashcards from GPT-OSS via Ollama API
├── main.py                 # Main entry point for the app
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Ollama installed on your system

### 1️⃣ Install Python Dependencies

```bash
pip install requests
```

### 2️⃣ Set Up Ollama

1. **Install Ollama** following the [official installation guide](https://ollama.ai/download)

2. **Pull the GPT-OSS model:**
   ```bash
   ollama pull gpt-oss
   ```

3. **Start the Ollama server:**
   ```bash
   ollama serve
   ```
   The server will run on `http://localhost:11434` by default.

### 3️⃣ Run the Application

```bash
python main.py
```

## 📖 Example Usage

```
=== AI Vocabulary Flashcard Trainer ===

Word: Serendipity
Definition: The occurrence of events by chance in a happy or beneficial way.
Example: It was pure serendipity that we met at the café.

Press Enter to see the next card...

Word: Ephemeral
Definition: Lasting for a very short time.
Example: The beauty of the sunset was ephemeral but breathtaking.

Press Enter to see the next card...

Do you wish to continue? (y/n): 
```

## ⚙️ How It Works

1. **Generation**: `flashcard_generator.py` sends a structured prompt to GPT-OSS via Ollama API
2. **Parsing**: The AI returns vocabulary flashcards in a specific text format that gets parsed
3. **Training**: `main.py` creates `Flashcard` objects and uses `FlashcardTrainer` to display them
4. **Interaction**: Users review cards one by one with interactive prompts

## 🛠️ Configuration

You can customize the application by modifying:

- **Model**: Change the model in `flashcard_generator.py` (requires compatible Ollama models)
- **Prompt**: Adjust the generation prompt for different topics or difficulty levels
- **Display**: Modify `flashcard_trainer.py` to change the review interface

## 📋 Requirements

- **Python**: 3.8+
- **Ollama**: Latest version
- **Model**: GPT-OSS (or compatible model)
- **Dependencies**: `requests` library

## 🚧 Troubleshooting

**Ollama not responding?**
- Ensure Ollama is running: `ollama serve`
- Check if the model is installed: `ollama list`

**Connection errors?**
- Verify Ollama is running on `http://localhost:11434`
- Check firewall settings

**No flashcards generated?**
- Ensure GPT-OSS model is properly installed
- Check the API response format in the generator

**Happy Learning! 📚✨**
