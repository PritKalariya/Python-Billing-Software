import os
from tkinter import *
from tkinter import messagebox


main = Tk()
main.geometry("1366x768")
main.title("Billing System")
main.resizable(0, 0)


def Exit():
    sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=main)
    if sure == True:
        main.destroy()

main.protocol("WM_DELETE_WINDOW", Exit)


def emp():
    main.withdraw()
    os.system("python employee.py")
    main.deiconify()


def adm():
    main.withdraw()
    os.system("python admin.py")
    main.deiconify()


label1 = Label(main)
label1.place(relx=0, rely=0, width=1366, height=768)
img = PhotoImage(file="./images/main.png")
label1.configure(image=img)


button1 = Button(main)
button1.place(relx=0.316, rely=0.446, width=146, height=90)
img2 = PhotoImage(file="./images/1.png")
button1.configure(
    relief="flat",
    cursor="hand2",
    activebackground="#fff",
    foreground="#fff",
    background="#fff",
    borderwidth="0",
    image=img2,
    command=emp
)


button2 = Button(main)
button2.place(relx=0.566, rely=0.448, width=146, height=90)
img3 = PhotoImage(file="./images/2.png")
button2.configure(
    relief="flat",
    overrelief="flat",
    activebackground="#ffffff",
    cursor="hand2",
    foreground="#ffffff",
    background="#ffffff",
    borderwidth="0",
    image=img3,
    command=adm,
)

main.mainloop()