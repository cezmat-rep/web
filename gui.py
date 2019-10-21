# from tkinter import *
#
# import tkinter
# root = Tk()
# frame = Frame(root)
# frame.pack()
# centerFrame = Frame(root)
# centerFrame.pack(anchor=CENTER)
# bbutton = Button(frame, text="Open", fg="blue")
# bbutton.pack()
# bbutton.place(anchor=CENTER)
# rbutton = Button(frame, text="close", fg="red")
# rbutton.pack(side=LEFT)
# gbutton = Button(centerFrame, text="send", fg="green")
# gbutton.pack(side=LEFT)
#
# blbutton = Button(centerFrame, text="reset",width=50)
# blbutton.pack(side=LEFT)
# root.mainloop()

from tkinter import *  # Use this if use python 3.xx
from tkinter.messagebox import showinfo

root = Tk()


def window(main):
    root.title("gui for stm")
    main.update_idletasks()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = screen_width / 2
    window_height = screen_width / 3
    window_position_x = screen_width / 2 - window_width / 2
    window_position_y = screen_height / 2 - window_height / 2
    root.geometry('%dx%d+%d+%d' % (window_width, window_height, window_position_x, window_position_y))


def send2(x):
    showinfo("Sending", "Now program will send information to modem %s" % x)
    print(x)

    E1.delete(0, END)


def send():
    showinfo("Sending", "Now program will send information to modem %s" % E1.get())
    print(E1.get())

    E1.delete(0, END)


def openT():
    showinfo("Opening transmission", "Now transmission will be open")
    E1.insert(0, "ramka na otwarcie transmisji")
    send2("ramka na otwarcie transmisji")


def reset():
    showinfo("Resetting modem", "Now modem will be restarted")
    E1.insert(0, "ramka na reset modemu")
    send2("ramka na reset modemu")


def close():
    showinfo("Good Bye!", "Now program will close")
    import sys;
    sys.exit()


window(root)
lc = Frame(root, height=400, )
lcr = Frame(lc, width=root.winfo_width() + root.winfo_width())
pc = Frame(root)
lcl = Frame(lc, width=root.winfo_width() + root.winfo_width())
lcl.pack(side=LEFT)
pcr = Frame(pc, width=root.winfo_width() + root.winfo_width())
pcr.pack(side=RIGHT)
# from Tkinter import *   # Use this if use python 2.xx
send = Button(lc, text="Send", fg="green", command=send, width=10, height=10)
send.pack(side=RIGHT)
openT = Button(pc, text="Open", fg="orange", command=openT, width=10, height=10)
openT.pack(side=LEFT)
close = Button(text="Close", fg="red", command=close, width=10, height=10)
close.pack()
reset = Button(text="reset", fg="red", command=reset, width=10, height=10)
reset.pack()
lc.pack(side=LEFT)
pc.pack(side=RIGHT)
L1 = Label(root, text="Wprowadź dane do wysania:")
L1.pack(side=LEFT)
E1 = Entry(root, bd=10)
E1.pack(side=RIGHT)

mainloop()
