import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess

# Function to check login
def check_login():
    # Get username and password from entry fields
    username = entry_username.get()
    password = entry_password.get()
    
    # Connect to MySQL database
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # your MySQL username
            password='Jbenitezxc18',  # your MySQL password
            database='user_db'
        )
        
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        
        if result:
            window.withdraw()
            messagebox.showinfo("Login Success", "Welcome to the system!")
            file_path = 'StudSelectSub.py'  # Modify this to your file's location
            subprocess.run(['python', file_path])
            
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
    
    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"Error: {err}")
    
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Setting up the tkinter window
window = tk.Tk()
window.title("Login System")
window.geometry("300x200")

# Username Label and Entry
label_username = tk.Label(window, text="Username:")
label_username.pack(pady=5)
entry_username = tk.Entry(window)
entry_username.pack(pady=5)

# Password Label and Entry
label_password = tk.Label(window, text="Password:")
label_password.pack(pady=5)
entry_password = tk.Entry(window, show="*")
entry_password.pack(pady=5)

# Login Button
login_button = tk.Button(window, text="Login", command=check_login)
login_button.pack(pady=20)

# Run the tkinter event loop
window.mainloop()
