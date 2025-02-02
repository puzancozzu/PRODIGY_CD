import tkinter as tk
from tkinter import filedialog
from xor_en_dc import xor_encrypt, xor_decrypt

def browse_file():
    file_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def perform_action():
    path = entry_path.get()
    key = int(entry_key.get())
    choice = action_var.get()

    if choice == 1:
        xor_encrypt(path, key)
    else:
        xor_decrypt(path, key)

# Create the main window
root = tk.Tk()
root.title("Image Encryption/Decryption")

# Create widgets
label_path = tk.Label(root, text="Image Path:")
entry_path = tk.Entry(root, width=40)
button_browse = tk.Button(root, text="Browse", command=browse_file)

label_key = tk.Label(root, text="Key:")
entry_key = tk.Entry(root, width=10)

label_action = tk.Label(root, text="Action:")
action_var = tk.IntVar()
radio_encrypt = tk.Radiobutton(root, text="Encryption", variable=action_var, value=1)
radio_decrypt = tk.Radiobutton(root, text="Decryption", variable=action_var, value=2)

button_execute = tk.Button(root, text="Execute", command=perform_action)

# Organize widgets using grid layout
label_path.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
entry_path.grid(row=0, column=1, padx=10, pady=5, columnspan=2)
button_browse.grid(row=0, column=3, padx=5, pady=5)

label_key.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
entry_key.grid(row=1, column=1, padx=10, pady=5)

label_action.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
radio_encrypt.grid(row=2, column=1, padx=5, pady=5)
radio_decrypt.grid(row=2, column=2, padx=5, pady=5)

button_execute.grid(row=3, column=0, columnspan=4, pady=10)

# Run the Tkinter event loop
root.mainloop()
