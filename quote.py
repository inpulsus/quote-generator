import requests
import random
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

def fetch_quotes():
    try:
        response = requests.get("https://type.fit/api/quotes")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Failed to fetch quotes: {e}")
        return []

def get_random_quote(quotes):
    if not quotes:
        return "No quotes available."
    quote = random.choice(quotes)
    author = quote["author"] if quote["author"] else "Unknown"
    return f'"{quote["text"]}"\n- {author}'

def display_quote():
    quote = get_random_quote(quotes)
    quote_label.config(text=quote)

def on_close():
    root.destroy()

# Fetch quotes at the beginning
quotes = fetch_quotes()

# Setup GUI
root = ttk.Window(themename="superhero")
root.title("Random Quote Generator")
root.geometry("600x400")

quote_label = ttk.Label(root, text="", wraplength=500, justify="center", font=("Helvetica", 14), bootstyle="inverse")
quote_label.pack(pady=50)

new_quote_button = ttk.Button(root, text="New Quote", command=display_quote, bootstyle="primary")
new_quote_button.pack(pady=20)

# Display an initial quote
display_quote()

# Handle window close event
root.protocol("WM_DELETE_WINDOW", on_close)

# Start the GUI event loop
root.mainloop()