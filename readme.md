# Voice Q&A Assistant (LLM + GUI + TTS)

This is a voice-enabled question-answering assistant with a graphical user interface. The app allows users to ask questions via voice, receive real-time answers from a language model (LLM), and hear the responses spoken aloud. Built using Python, OpenAI API, Tkinter, and text-to-speech libraries.

## Features

- Voice input through your microphone
- Real-time streaming answers from an LLM (e.g., GPT-3.5)
- Text-to-speech playback of the model’s answer
- GUI built with Tkinter for ease of use
- Stop button to interrupt speech output

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/voice-qa-assistant.git
cd voice-qa-assistant
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your OpenAI API key:

Create a file named `config.py` In the root directory with the following content:

```python
OPENAI_API_KEY = "your_api_key_here"
```

Alternatively, you can use environment variables if preferred.

## Usage

Run the application:

```bash
python main.py
```

A window will appear with buttons to ask a question and stop the speech output. Click "Ask Question" to speak your question. The app will transcribe your speech, send it to the LLM, display the response, and read it aloud.

## Project Structure

```
voice-qa-assistant/
├── main.py                 # GUI application entry point
├── config.py               # Contains API key
├── requirements.txt        # Python dependencies
└── utils/
    ├── transcribe.py       # Voice input and speech recognition
    ├── query_llm.py        # LLM API integration
    ├── speak.py            # Text-to-speech playback
```

## Dependencies

- Python 3.10+
- openai
- speechrecognition
- pyttsx3
- tkinter (standard with Python)
- pyaudio (for microphone input)

## Notes

- Requires an internet connection to access the language model.
- Tested on Windows with Python 3.12.
- Works without a GPU.


