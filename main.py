import tkinter as tk
from tkinter import scrolledtext
import threading

from utils.transcribe import get_voice_input
from utils.query_llm import stream_llm_response
from utils.speak import speak
from utils.speak import stop_speaking

class VoiceQAGUI:
    def __init__(self, root):
        self.root = root
        root.title("🧠 Voice Q&A Assistant")
        root.geometry("600x400")
        self.stop_button = tk.Button(root, text="🔇 Stop Speaking", command=self.stop_speech, font=("Arial", 12), bg="#f44336", fg="white")
        self.stop_button.pack(pady=5)

        self.ask_button = tk.Button(root, text="🎤 Ask Question", command=self.ask_question, font=("Arial", 14), bg="#4CAF50", fg="white")
        self.ask_button.pack(pady=10)

        self.output = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 12))
        self.output.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        

    def ask_question(self):
        threading.Thread(target=self.process_question, daemon=True).start()

    def process_question(self):
        self.ask_button.config(state=tk.DISABLED)
        self.output.insert(tk.END, "🎤 Listening...\n")
        self.output.see(tk.END)

        question = get_voice_input()
        self.output.insert(tk.END, f"\n🧍 You: {question}\n")
        self.output.insert(tk.END, "🤖 Answering...\n")
        self.output.see(tk.END)

        full_answer = ""
        for chunk in stream_llm_response(question):
            full_answer += chunk
            self.output.insert(tk.END, chunk)
            self.output.see(tk.END)

        speak(full_answer)
        self.output.insert(tk.END, "\n" + "-" * 50 + "\n")
        self.ask_button.config(state=tk.NORMAL)

    def stop_speech(self):
        stop_speaking()


if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceQAGUI(root)
    root.mainloop()
