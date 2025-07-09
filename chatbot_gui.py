import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import ollama

# --- Dark Mode Colors ---
BG_COLOR = "#1e1e1e"
TEXT_COLOR = "#d4d4d4"
ENTRY_BG = "#2d2d2d"
BUTTON_BG = "#3c3c3c"
BUTTON_FG = "#97238F"  # Your custom button text color
FONT = ("Consolas", 12)

# Initialize chat history
chat_history = [
    {'role': 'system', 'content': 'You are a US president.'}
]

# Function to send message and get response
def send_message():
    user_input = entry.get()
    if not user_input.strip():
        return

    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "You: " + user_input + "\n")
    chat_display.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

    chat_history.append({'role': 'user', 'content': user_input})
    response = ollama.chat(model='mistral', messages=chat_history)
    reply = response['message']['content']
    chat_history.append({'role': 'assistant', 'content': reply})

    chat_display.config(state=tk.NORMAL)
    chat_display.insert(tk.END, "Bot: " + reply + "\n\n")
    chat_display.config(state=tk.DISABLED)
    chat_display.see(tk.END)

# GUI setup
root = tk.Tk()
root.title("Offline Chatbot (Ollama + Python)")
root.geometry("500x500")
root.configure(bg=BG_COLOR)

# Chat display box
chat_display = ScrolledText(
    root,
    wrap=tk.WORD,
    font=FONT,
    bg=BG_COLOR,
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR
)
chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Text input field
entry = tk.Entry(
    root,
    font=FONT,
    bg=ENTRY_BG,
    fg=TEXT_COLOR,
    insertbackground=TEXT_COLOR
)
entry.pack(padx=10, pady=(0, 10), fill=tk.X)
entry.bind("<Return>", lambda event: send_message())

# Send button
send_button = tk.Button(
    root,
    text="Send",
    command=send_message,
    font=FONT,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    activebackground=ENTRY_BG
)
send_button.pack(padx=10, pady=(0, 10))

# Run the GUI app
root.mainloop()
