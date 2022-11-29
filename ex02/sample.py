import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt,f"{txt}ボタンが押されました")

root = tk.Tk()
root.title("おためしか")
root.geometry("300x500")

button = tk.Button(root, text="押すな")
button.bind("<1>",button_click)
button.pack()



entry = tk.Entry(width=30)
entry.insert(tk.END,"fugapiyo")
entry.pack()

root.mainloop()