import tkinter as tk
from tkinter import messagebox


quizzes = {
    "English": ["Question 1 for English", "Question 2 for English"],
    "Science": ["Question 1 for Science", "Question 2 for Science"],
    "Math": ["Question 1 for Math", "Question 2 for Math"],
    "Social Studies": ["Question 1 for Social Studies", "Question 2 for Social Studies"]
}

def start_quiz(subject):
    questions = quizzes.get(subject, [])
    if questions:
        messagebox.showinfo("Quiz", f"Starting {subject} quiz!\nFirst question: {questions[0]}")
    else:
        messagebox.showinfo("Quiz", f"No quiz available for {subject}")


root = tk.Tk()
root.title("Quiz Application")
root.geometry("400x300")
root.configure(bg="#D1C4E9")


bg_color = "#D1C4E9"
button_bg = "#7E57C2"
button_fg = "#FFFFFF"

frame = tk.Frame(root, bg=bg_color)
frame.pack(expand=True, anchor=tk.CENTER)

subjects = ["English", "Science", "Math", "Social Studies"]
for subject in subjects:
    button = tk.Button(frame, text=subject, command=lambda s=subject: start_quiz(s), bg=button_bg, fg=button_fg, width=20, height=2)
    button.pack(pady=10)

root.mainloop()
