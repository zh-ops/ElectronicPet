import tkinter as tk


def main():
    root = tk.Tk()
    root.title("电子宠物")
    root.geometry('960x684')

    #bg_path = '../picture/bg.gif'
    #bg_open = tk.PhotoImage(file=bg_path)
    #bg = tk.Label(root, image=bg_open, )
    # bg.pack()
    # 背景会遮住元素，去掉。

    dog_path = '../picture/normal_dog.gif'
    dog_photo = tk.PhotoImage(file=dog_path)
    dog = tk.Label(root, image=dog_photo)
    dog.pack(side=tk.LEFT)

    root.mainloop()


if __name__ == "__main__":
    main()
