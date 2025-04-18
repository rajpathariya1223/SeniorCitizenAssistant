import tkinter as tk
from tkinter import messagebox

def launch_gui():
    root = tk.Tk()
    root.title("Senior Citizen Assistant")
    root.geometry("500x400")
    root.configure(bg="#f0f0f0")

    title = tk.Label(root, text="Welcome to Senior Assistant", font=("Arial", 20, "bold"), bg="#f0f0f0")
    title.pack(pady=20)

    tk.Button(root, text="🕒 Set Medication Reminder", font=("Arial", 14), width=30, command=lambda: messagebox.showinfo("Reminder", "Feature coming soon")).pack(pady=10)
    tk.Button(root, text="📞 Emergency Contact", font=("Arial", 14), width=30, command=lambda: messagebox.showinfo("Emergency", "Feature coming soon")).pack(pady=10)
    tk.Button(root, text="🎙️ Talk to Assistant", font=("Arial", 14), width=30, command=lambda: messagebox.showinfo("Voice", "Feature coming soon")).pack(pady=10)

    root.mainloop()
