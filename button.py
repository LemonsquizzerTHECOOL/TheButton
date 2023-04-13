import tkinter as tk

def change_label_text():
    label.config(text="Wow, you clicked a button! You must be so proud...")

window = tk.Tk()
window.title("Useless Button")

label = tk.Label(window, text="Click The Button That Says 'Click me!'", font=("Helvetica", 20))
label.pack(pady=20)

button = tk.Button(window, text="Click me!", command=change_label_text)
button.pack()

window.mainloop()
