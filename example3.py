


from tkinter import Text, Tk
r = Tk()

def openandreadfile():
    with open("C:/DjangoPython/tkinter/test.txt") as myfile:
        t.insert("1.0", myfile.read())


t = Text()
t.grid()



openandreadfile()

r.mainloop()
