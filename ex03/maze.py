import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym

    #こうかとんが移動すると色が変わる
    canvas.create_rectangle(mx*80, my*80, mx*80+80, my*80+80, fill = "#b0c4de")

def key_up(event):
    global key
    key = ""

def main_proc():
    global cx,cy,mx,my

    #スタートのお知らせ(無限ループする)
    # while True:
    #     if mx ==1 and my == 1:
    #         tkm.showinfo("スタート","スタート")
    #         break
    
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if maze_lst[mx][my] == 1:
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
    
    cx,cy = mx * 80 + 40,my * 80 + 40
    
    #ゴールのお知らせ
    # if cx == 14:
    #     tkm.showinfo("おめでとう","ゴールだよ")

    canvas.coords("kokaton",cx,cy)

    #こうかとんを最前面に配置する
    canvas.lift("kokaton")
    
    root.after(100,main_proc)
 
if __name__ == "__main__":
    root = tk.Tk()
    root.title("迷えるこうかとん")
    canvas = tk.Canvas(root,width=1200,height=900,bg="black")
    canvas.pack()

    maze_lst = mm.make_maze(15,9)
    mm.show_maze(canvas,maze_lst)

    mx,my = 1,1
    cx,cy = mx * 80 + 40,my * 80 + 40
    
    tori = tk.PhotoImage(file="fig/8.png")
    canvas.create_image(cx,cy,image=tori,tag="kokaton")
    key = ""
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)
    main_proc()
    root.mainloop() 