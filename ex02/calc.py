import tkinter as tk
import tkinter.messagebox as tkm

#練習3
def button_click(event):
    btn = event.widget
    num = btn["text"]
    if num =="=":
        
        siki = entry.get()
        res = eval(siki)
        entry.delete(0, tk.END)
        entry.insert(tk.END,res)
    
    elif num == "+/-":
        fugo = entry.get()
        gyaku = int(fugo) * -1
        entry.delete(0, tk.END)
        entry.insert(tk.END,gyaku)

        

    elif  num == "AC":
        entry.delete(0,tk.END)
    
    elif  num == "C":
        delete = entry.get()
        entry.delete(len(delete)-1,tk.END)

    else:
    #tkm.showinfo("",f"{num}ボタンがクリックされました")
    #練習6
        entry.insert(tk.END,num)

def b_over(event):
    event.widget["bg"] = "#b0c4de"

def b_leave(event):
    event.widget["bg"] = "SystemButtonFace"
    
    

#練習1
root = tk.Tk()
root.geometry("400x700")
root.title("電卓")

entry= tk.Entry(root,justify="right",width=10,font = ("",40))
entry.grid(row=0,column=0,columnspan=4)


#練習2
r,c = 2,0
suuzi =[7,8,9,4,5,6,1,2,3]
for num in suuzi:
    button = tk.Button(root, text=f"{num}",width=4,height=2,font=("",30))
    button.grid(row = r,column =c)
    button.bind("<1>",button_click)
    button.bind("<Enter>",b_over)
    button.bind("<Leave>",b_leave)
    c += 1
    if c%3 == 0:
        r += 1
        c =0
r,c = 5,1


#練習5
operators = ["+","-","*","/","="]
r,c =2,3
for ope in operators:
    button = tk.Button(root, text=f"{ope}",width=4,height=2,font=("",30))
    button.grid(row = r,column =c)
    button.bind("<1>",button_click)
    button.bind("<Enter>",b_over)
    button.bind("<Leave>",b_leave)
    if c%3 == 0:
        r += 1

deleter = ["AC","C"]
r,c =1,2
for de in deleter:
    button = tk.Button(root, text=f"{de}",width=4,height=2,font=("",30))
    button.grid(row = r,column =c)
    button.bind("<1>",button_click)
    button.bind("<Enter>",b_over)
    button.bind("<Leave>",b_leave)
    c += 1

ten = ["+/-",0,"."]
r,c =5,0
for t in ten:
    button = tk.Button(root, text=f"{t}",width=4,height=2,font=("",30))
    button.grid(row = r,column =c)
    button.bind("<1>",button_click)
    button.bind("<Enter>",b_over)
    button.bind("<Leave>",b_leave)
    c += 1
    

root.mainloop()
    