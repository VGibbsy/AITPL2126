from tkinter import *
a=Tk()
a.title("Notepad")
a.geometry("300x300+50+50")
m1=Menu()
l1=Menu()
l2=Menu()
l3=Menu()
l4=Menu()
l5=Menu()

m1.add_cascade(label="File",menu=l1)
m1.add_cascade(label="Edit",menu=l2)
m1.add_cascade(label="Format",menu=l3)
m1.add_cascade(label="View",menu=l4)
m1.add_cascade(label="Help",menu=l5)

l1.add_command(label="NewFile")
l1.add_command(label="OpenFile")
l1.add_command(label="SaveFile")

l2.add_command(label="Copy")
l2.add_command(label="Paste")
l2.add_command(label="Undo")

l3.add_command(label="Wordwrap")
l3.add_command(label="Font")

l4.add_command(label="Zoom")
l4.add_command(label="Statusbar")

l5.add_command(label="Viewhelp")
l5.add_command(label="Feedback")

a.config(menu=m1)
a.mainloop()