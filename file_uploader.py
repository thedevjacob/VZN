import tkinter as tk
from tkinter import filedialog
from PIL import Image
from ai_interpreter import interpret_image

filepath = ""

def upload_file():
    global filepath
    filepath = ""
    while not filepath:
        filepath = filedialog.askopenfilename(
            defaultextension=".png .jpg .jpeg",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg"), ("All Files", "*.*")]
        )
        if filepath:
            image_check = is_valid_image(filepath)
            if image_check is not True:
                tk.messagebox.showerror("Error", f"Failed to load file:\n{image_check}")
        else:
            break
    window.destroy()
    return filepath


def is_valid_image(filename):
    try:
        Image.open(filename).verify()
        return True
    except Exception as exception:
        return exception

window = tk.Tk()
window.title("File Uploader")

choices = ['Explain', 'Solve', 'Describe']
variable = tk.StringVar(window)
w = tk.OptionMenu(window, variable, *choices)
w.pack(pady=20)

upload_button = tk.Button(window, text="Upload File", command=upload_file)
upload_button.pack(pady=20)

window.mainloop()

if filepath:
    print(interpret_image(filepath, variable.get()).interpretation_text)
