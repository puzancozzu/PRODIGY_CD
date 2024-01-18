
### USINF TKINTER  fro UI

import tkinter as tk
from tkinter import font
from caesar_cipher_algorithm import encrypt, decrypt, Error

def perform_operation():

    inputted_text = text_entry.get()

    shift_value = int(shift_entry.get())

    choice = operation_choice.get()


    if choice == 1:

        result.set(encrypt(inputted_text, shift_value))

    elif choice == 2:

        result.set(decrypt(inputted_text, shift_value))
    
    else:
        result.set("Selete Operation")

### to validate only numeric shift values are accepted
        
def validate_input(char, entry_value):
    return char.isdigit()

### Title of UI BOX
root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption")

custom_font = font.Font(family="Comic Sans MS", size=12)

### for Input text Section
text_label = tk.Label(root, text="Enter Text:", font=custom_font)
text_label.grid(row=0, column=0, padx=20, pady=10)

text_entry = tk.Entry(root, width =40, font=custom_font)
text_entry.grid(row=0, column=1, padx=20, pady=10)


### for Selection of Shift Value
shift_label = tk.Label(root, text="Enter Shift Value:", font=custom_font)
shift_label.grid(row=1, column=0, padx=20, pady=10)

validate_cmd = root.register(validate_input)

# shift_entry = tk.Entry(root)
shift_entry = tk.Entry(root, validate="key", validatecommand=(validate_cmd, '%S', '%P'))

shift_entry.grid(row=1, column=1, padx=20, pady=10)


### for selection of type of opertion to perform
operation_label = tk.Label(root, text="Select Operation:" , font=custom_font)
operation_label.grid(row=2, column=0, padx=10, pady=10)

operation_choice = tk.IntVar()
encryption_radio = tk.Radiobutton(root, text="Encryption", variable=operation_choice, value=1, font=custom_font)
encryption_radio.grid(row=2, column=1, padx=0, pady=10)
decryption_radio = tk.Radiobutton(root, text="Decryption", variable=operation_choice, value=2, font=custom_font)
decryption_radio.grid(row=2, column=2, padx=0, pady=10)



### to initate opertaion
perform_button = tk.Button(root, text="Encrypt/Decrypt", command=perform_operation, font=custom_font, bg='#66cf0a')
perform_button.grid(row=3, column=0, columnspan=3, pady=10)


### to print the result
result_label = tk.Label(root, text="Result:", font=custom_font)
result_label.grid(row=4, column=0, padx=20, pady=10)

result = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result, state="readonly", font=custom_font, width=40)
result_entry.grid(row=4, column=1, padx=20, pady=10)


root.mainloop()


