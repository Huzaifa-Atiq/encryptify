import customtkinter as ctk




def switch_mode():
    if mode.get() == "Encryption":
        mode.set("Decryption")
        label_mode.configure(text="Mode: Decryption")
        submit_button.configure(text="Decrypt")
       
    else:
        mode.set("Encryption")
        label_mode.configure(text="Mode: Encryption")
        submit_button.configure(text="Encrypt")


       
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("Encryptify")
app.geometry("1280x720")


mode = ctk.StringVar(value="Encryption")


#Mode
label_mode = ctk.CTkLabel(app, text=f"Mode: {mode.get()}", font=("Arial", 20))
label_mode.pack(pady=40)

#file path
label_path = ctk.CTkLabel(app, text="file path", font=("Arial", 12))
label_path.pack(pady=1)
path = ctk.CTkEntry(app, width=300, placeholder_text="Enter file path")
path.pack()

#password
label_pass = ctk.CTkLabel(app, text="password", font=("Arial", 12))
label_pass.pack(pady=1)
password = ctk.CTkEntry(app, width=300, placeholder_text="password")
password.pack()

submit_button = ctk.CTkButton(app, text="Encrypt",fg_color="green", command=switch_mode)
submit_button.pack(pady=10)

toggle_button = ctk.CTkButton(app, text="Switch Mode", command=switch_mode)
toggle_button.pack(pady=10)

app.mainloop()