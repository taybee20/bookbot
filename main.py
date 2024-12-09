import tkinter as tk
from tkinter import filedialog, messagebox, Text
import os

# GUI Class
class TextAnalyzerApp:
    def __init__(self, root):
        # Makes main window available everywhere in class
        self.root = root
        self.root.title("Bookbot")

        # Create a file upload button 
        self.upload_button = tk.Button(root, text="Upload Text File", padx=20, pady=10, command=self.upload_files)
        # Places button on screen
        self.upload_button.pack()

        
        # Text widget to display analysis results
        self.result_text = tk.Text(root, height=30, width=100)
        self.result_text.pack()

    def upload_files(self):
        """Handles the file upload."""
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])

        if file_path:
            self.analyze_text(file_path)

    def analyze_text(self, file_path):
        """Reads, analyzes, and displays the results of the text file."""
        text = get_book_text(file_path)
        word_count = wordcount(text)
        char_list = character_count(text)

        char_list.sort(reverse=True, key=sort_on)

        # Displaying report
        self.result_text.delete("1.0", tk.END)  # Clear any previous analysis
        self.result_text.insert(tk.END, f"--- Begin report of {file_path} ---\n\n")
        self.result_text.insert(tk.END, f"{word_count} words found in the document\n\n")

        for char in char_list:
            c = char["name"]
            count = char["count"]
            self.result_text.insert(tk.END, f"The '{c}' character was found {count} times\n")

# Analysis functions 
def sort_on(dict):
    return dict["count"]

def wordcount(book):
    words = book.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_count(book):
    characters = {}
    
    for c in book: 
        char = c.lower()

        if char.isalpha():
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

    char_list = [{"name": k, "count": v} for k, v in characters.items()]
    return char_list

if __name__ == "__main__":
    root = tk.Tk()
    app = TextAnalyzerApp(root)
    root.mainloop()