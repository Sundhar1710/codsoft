import tkinter as tk
import random

def play(choice):
    option = ["rock", "paper", "scissor"]
    com_choice = random.choice(option)
    if choice == com_choice:
        res = "It's a Tie.."
        color = "black"
    elif choice == "rock" and com_choice == "scissor":
        res = "You Win"
        color = "green"
    elif choice == "paper" and com_choice == "rock":
        res = "You Win"
        color = "green"
    elif choice == "scissor" and com_choice == "paper":
        res = "You Win"
        color = "green"
    else:
        res = "Computer Wins"
        color = "red"
    
    res_label.config(
        text = f"You chose: {choice.upper()} | Computer chose: {com_choice.upper()}\n\n{res}",
        fg = color
    )

r = tk.Tk()
r.title("Rock Paper Scissors")
r.geometry("400x300")
r.config(bg="#f0f0f0")

title = tk.Label(r, text="Rock Paper Scissors Game", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

button_frame = tk.Frame(r, bg="#f0f0f0")
button_frame.pack(pady=10)

btn_font = ("Arial", 12, "bold")
tk.Button(button_frame, text="Rock", width=10, font=btn_font, bg="#d1e7dd", command=lambda:play("rock")).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Paper", width=10, font=btn_font, bg="#cfe2ff", command=lambda:play("paper")).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Scissor", width=10, font=btn_font, bg="#f8d7da", command=lambda:play("scissor")).grid(row=0, column=2, padx=10)

res_label = tk.Label(r, text="", font=("Arial", 14), bg="#f0f0f0", justify="center")
res_label.pack(pady=30)

r.mainloop()
