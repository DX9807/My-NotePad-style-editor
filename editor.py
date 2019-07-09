from tkinter import *
from tkinter.ttk import *
from tkinter.commondialog import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.scrolledtext import *



root = Tk()

root.iconbitmap('Bokehlicia-Pacifica-Accessories-text-editor.ico')
root.minsize(height = 600, width = 600)

filename = None

def open_file():

    global filename
    filename = askopenfilename(filetypes = (("Python Stuff",".PY"),("All files","*.*")))
    print(filename)
    text_box.delete("1.0", END)
    root.title('MyEditor |{}'.format(filename))
    with open(filename) as file:
        text_box.insert(END,file.read())



def save_file():
    global filename
    with open(filename,'w+') as file:

        if file is None:
            return
        text_to_save = str(text_box.get('1.0',END))
        file.write(text_to_save)
        file.close()




def save_file_as():
    global filename
    filename = asksaveasfile(mode = "w")
    if filename is None:
        return
    file_to_save=str(text_box.get('1.0',END))
    filename.write(file_to_save)
    filename.close()


def create_file():
    global filename
    filename = "C:/Users/Subodh/Documents/{}".format("myeditor.txt")
    root.title('MyEditor |{}'.format(filename))
    with open(filename,'w+') as file:
        text_to_save = str(text_box.get('1.0',END))
        file.write(text_to_save)
        file.close()


def print_file():
    pass

def clear():
    text_box.delete(0.0, END)

def redo():
    text_box.edit_redo()

def undo():
    text_box.edit_undo()




top = Menu(root)                                # win=top-level window
root.config(menu=top)

file = Menu(top)
file.add_separator()
file.add_command(label='New',  command=create_file,  underline=0)
file.add_separator()
file.add_command(label='Open', command=open_file,  underline=0)
file.add_separator()
file.add_command(label='Save', command=save_file,  underline=0)
file.add_separator()
file.add_command(label='Save As', command=save_file_as,  underline=0)
file.add_separator()
file.add_command(label='Print', command=print_file,  underline=0)
file.add_separator()
file.add_command(label='Quit',    command=root.quit, underline=0)
file.add_separator()
top.add_cascade(label='File',     menu=file,        underline=0)

edit = Menu(top, tearoff=False)
edit.add_separator()
edit.add_command(label='Undo',     command=undo,  underline=0)
edit.add_separator()
edit.add_command(label='Redo',     command=redo,  underline=0)
edit.add_separator()
edit.add_command(label='Cut',     command=None,  underline=0)
edit.add_separator()
edit.add_command(label='Paste',   command=None,  underline=0)
edit.add_separator()
edit.add_command(label='Clear',     command=clear,  underline=0)
edit.add_separator()
edit.add_command(label='Select All',     command=None,  underline=0)
edit.add_separator()
edit.add_command(label='Find Next',     command=None,  underline=0)
edit.add_separator()
edit.add_command(label='Find',     command=None,  underline=0)
edit.add_separator()
edit.add_command(label='Replace',     command=None,  underline=0)
edit.add_separator()
edit.add_command(label='GoTo',     command=None,  underline=0)
edit.add_separator()
top.add_cascade(label='Edit',     menu=edit,        underline=0)


format = Menu(top, tearoff=False)
format.add_separator()
format.add_command(label='Word Wrap',     command=None,  underline=0)
format.add_separator()
format.add_command(label='Font..',     command=None,  underline=0)
format.add_separator()
top.add_cascade(label='Format',     menu=format,        underline=0)

view = Menu(top, tearoff=False)
view.add_separator()
view.add_command(label='StatusBar',     command=None,  underline=0)
view.add_separator()
top.add_cascade(label='View',     menu=view,        underline=0)

help = Menu(top, tearoff=False)
help.add_command(label='View Help',     command=None,  underline=0)
help.add_separator()
help.add_command(label='About MyEditor',     command=None,  underline=0)
help.add_separator()
top.add_cascade(label='Help',     menu=help,        underline=0)

text_box = ScrolledText(master=root)
text_box.config(height=200,width=200)
text_box.pack()






root.title('MyEditor')
root.mainloop()
