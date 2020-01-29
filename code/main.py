import tkinter as tk

root = tk.Tk()
root.title("电子宠物")
root.geometry('960x684')

bg_path = '../picture/bg.gif'
bg_open = tk.PhotoImage(file=bg_path)
bg = tk.Label(root, image=bg_open, compound=tk.CENTER)
bg.pack()

dog_path = '../picture/normal_dog.gif'


root.mainloop()