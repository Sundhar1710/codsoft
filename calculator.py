import tkinter as tk

def click(event):
    current = str(entry.get())
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.config(bg="#f5f5f5")

entry = tk.Entry(root, font=("Arial", 20), bd=8, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, ipady=8, pady=10, padx=10)

btn_texts = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["C", "0", ".", "/"],
    ["%", "=", "", ""]
]

for row in btn_texts:
    frame = tk.Frame(root, bg="#f5f5f5")
    frame.pack(expand=True, fill="both")
    for text in row:
        if text != "":
            btn = tk.Button(frame,text=text,font=("Arial", 16),relief=tk.RAISED,bd=4,bg="#e0e0e0",
            activebackground="#d0d0d0")
            btn.pack(side="left", expand=True, fill="both", padx=2, pady=2)
            btn.bind("<Button-1>", click)

root.mainloop()
