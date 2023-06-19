# complete by july 19th 

import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x300")
root.title("notes app")

note_text = tk.Text(root)
note_text.pack(fill=tk.BOTH, expand=True)

def save_note():
    note_content = note_text.get("1.0", tk.END)
    with open("note.txt", "w") as file:
        file.write(note_content)
    messagebox.showinfo("Note Saved", "The note has been saved successfully.")

menubar = tk.Menu(root)
root.config(menu=menubar)

file_menu = tk.Menu(menubar)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_note)

root.mainloop()
