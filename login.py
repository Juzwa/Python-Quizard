import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Basic login credentials check
    if username == "user" and password == "pass":
        messagebox.showinfo("Login Status", "Login Successful!")
    else:
        messagebox.showerror("Login Status", "Invalid credentials, please try again.")

# Create the main window
root = tk.Tk()
root.title("Minimalist Login Window")
root.geometry("300x200")

# Username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=10)
entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=20)

# Run the application
root.mainloop()
