# GNB - 1st - GUI Notes
import tkinter as tk

root = tk.Tk()


root.title("Testing")
root.configure(background = "orange")
root.minsize = (250, 250)
root.maxsize = (670, 670)
root.geometry("300x300+100+100")
#everything we want should be inbetween these two commands
label = tk.Label(root, text = "This is currently working :)", font = ("", 67, "bold"))
label.config(fg = "turquoise", background = "orange")
label.pack()
#image = tk.PhotoImage(file = "notes\pngtree-fried-chicken-png-png-image_14516402.png")
#tk.Label(root, image = image).pack()

#Stuff about button
root.count = 0
def add():
    root.count += 1
    num["text"] = root.count
  #  tk.Label(root, text = root.count).pack()


btn = tk.Button(root, text = "ADD", command = add)
btn.pack()
num = tk.Label(root, text = "0")
num.pack()
label.pack()

root.mainloop()