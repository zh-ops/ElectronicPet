import tkinter as tk


def main():
    root = tk.Tk()
    root.title("电子宠物")
    root.geometry('960x680')

    dog_photo = tk.PhotoImage(file='normal_dog.gif')
    dog = tk.Label(root, image=dog_photo)
    dog.place(x=0, y=(680-288)//2)

    eat_button = tk.Button(root, text='吃饭')
    play_button = tk.Button(root, text='玩耍')
    seedoctor_button = tk.Button(root, text='看病')
    walk_button = tk.Button(root, text='散步')
    eat_button.place(x=288+50, y=((680-288)//2)-50)
    play_button.place(x=288+50, y=((680-288)//2)+50)
    seedoctor_button.place(x=288+50, y=((680-288)//2)+150)
    walk_button.place(x=288+50, y=((680-288)//2)+250)
    root.mainloop()


if __name__ == "__main__":
    main()
