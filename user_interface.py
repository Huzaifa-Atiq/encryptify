import customtkinter as ctk
from tkinter import filedialog
import logic


def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=[("All Files", "*.*")]
    )
    if file_path:
        path_input.delete(0, ctk.END)
        path_input.insert(0, file_path)


def submit_encrypt():
    path = path_input.get()
    password = password_input.get()

    if path == "" or password == "":
        success_label.configure(text='file path or password not provided',text_color="#ca0f0f")

    else:
        path_input.delete(0, ctk.END)
        password_input.delete(0, ctk.END)

        result = logic.encrypt_file(path, password)

        if result == True:
            success_label.configure(text='Encrypted file successfully saved at the path',text_color="#32CD32")
        else:
            success_label.configure(text='Unexpected error',text_color="#ca0f0f")


def submit_decrypt():
    path = path_input.get()
    password = password_input.get()

    if path == "" or password == "":
        success_label.configure(text='file path or password not provided',text_color="#ca0f0f")

    else:
        path_input.delete(0, ctk.END)
        password_input.delete(0, ctk.END)

        result = logic.decrypt_file(path, password)

        if result == True:
            success_label.configure(text='File successfully decrypted and saved at the path',text_color="#32CD32")
        else:
            success_label.configure(text='Unexpected error',text_color="#ca0f0f")

def switch_mode():
    if mode.get() == "Encryption":
        mode.set("Decryption")
        label_mode.configure(text="Mode: Decryption")
        submit_button.configure(text="Decrypt",command=submit_decrypt)
       
    else:
        mode.set("Encryption")
        label_mode.configure(text="Mode: Encryption")
        submit_button.configure(text="Encrypt",command=submit_encrypt)


       
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Encryptify")
app.geometry("1280x720")


mode = ctk.StringVar(value="Encryption")


#Mode
label_mode = ctk.CTkLabel(app, text=f"Mode: {mode.get()}", font=("Arial", 20))
label_mode.pack(pady=40)

# file path
label_path = ctk.CTkLabel(app, text="File Path", font=("Arial", 12))
label_path.pack(pady=1)

path_frame = ctk.CTkFrame(app)
path_frame.pack()

path_input = ctk.CTkEntry(path_frame, width=350, placeholder_text="Select file...")
path_input.pack(side="left", padx=5)

browse_button = ctk.CTkButton(path_frame, text="Browse", width=80, command=browse_file)
browse_button.pack(side="left", padx=5)


#password
label_pass = ctk.CTkLabel(app, text="password", font=("Arial", 12))
label_pass.pack(pady=1)
password_input = ctk.CTkEntry(app, width=300, placeholder_text="password")
password_input.pack()

submit_button = ctk.CTkButton(app, text="Encrypt",fg_color="green", command=submit_encrypt)
submit_button.pack(pady=10)

toggle_button = ctk.CTkButton(app, text="Switch Mode", command=switch_mode)
toggle_button.pack(pady=10)

success_label = ctk.CTkLabel(app, text="", font=("Arial", 16, "bold"))
success_label.pack(pady=0)

app.mainloop()