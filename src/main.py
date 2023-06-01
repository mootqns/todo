import tkinter as tk

def toggle_fullscreen(event):
    # Toggle fullscreen mode
    root.attributes("-fullscreen", not root.attributes("-fullscreen"))

root = tk.Tk()

# Bind Escape key to exit fullscreen mode
root.bind("<Escape>", toggle_fullscreen)

# Create a Text widget!!!!!!!!!!!!!!
text_box = tk.Text(root)
text_box.pack(fill="both", expand=True)

# Configure the root window for fullscreen
root.attributes("-fullscreen", True)

root.mainloop()
