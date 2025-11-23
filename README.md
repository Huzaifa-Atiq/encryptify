# Encryptify

Encryptify is a desktop application for securely encrypting and decrypting any type of file using a password.  
It uses **AES-256-GCM** along with **PBKDF2-HMAC-SHA256** to ensure strong encryption, integrity protection, and safe password-based key generation.  
The interface is built with **CustomTkinter** for a clean and modern UI.

---

## 🔐 Features

### File Encryption
- AES-256-GCM encryption
- Random salt + nonce generated for every file
- Protects against modification and wrong password attempts
- Appends metadata to store the original file extension
- Outputs encrypted files as `.efy` (custom extension)

### File Decryption
- Automatically restores the original extension (e.g., `.png`, `.mp4`, `.pdf`)
- Fails safely if password is wrong
- Works on all file types since everything is handled in binary

### Modern GUI
- Built with **CustomTkinter**
- Dark mode
- Easy file path and password inputs
- Dynamic mode switch: Encryption ↔ Decryption
- Success and error messages

---

## 🛠️ How It Works

1. **Key Derivation:**  
   Uses `PBKDF2-HMAC-SHA256` to derive a 32-byte key from the password.  
   A random **salt (16 bytes)** ensures unique keys even for identical passwords.

2. **Encryption:**  
   AES-GCM uses a random **nonce (12 bytes)** to encrypt the file.

3. **Output Format:**  
   [salt][nonce][extension_length][extension][ciphertext]


4. **AES-GCM Guarantees:**  
- Confidentiality  
- Integrity  
- Authenticity (wrong password = TagError)

---

## 📁 Project Structure

- **user_interface.py** — Handles the GUI and calls logic functions.  
- **logic.py** — Handles encryption, decryption, metadata extraction, salt/nonce, and file reconstruction.

---

## 🧪 What I Learned

- AES-GCM encryption and authentication
- Using salts, nonces, and key derivation for security
- Binary file handling in Python
- Designing GUIs with CustomTkinter
- Structuring multi-file Python applications
- Building and packaging Python apps

---

## ▶️ How to Run

### Option 1 — Run the EXE
Download the precompiled `.exe` file from the releases page and simply run it.  
(No installation required.)

### Option 2 — Run the Source Code
```bash
pip install cryptography customtkinter
python user_interface.py
```

## 🚧 Possible Improvements

- Drag-and-drop file support
- Folder encryption
- Progress indicator
- Themes (light/dark toggle)
- Password strength meter
- "Remember last file" option
- File chooser dialog instead of text input

If you find **Encryptify** useful, please consider giving it a ⭐ on GitHub! Your support is greatly appreciated.

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

