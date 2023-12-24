from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog
from tkinter import ttk
from tkinter import font
import time, os
global selected
selected = False
global filepath
filepath = False


def save(__init__):
    global savefile
    savefile = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Text file", ".txt"), ("All files", ".*")], title='Save File', initialdir='~')
    savefiletext = str(text.get(1.0,END))
    savefile.write(savefiletext)
    savefile.close()
    file_name.config(text='File was saved!')
def saveas(__init__):
    text_file = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[("Text file", ".txt"), ("All files", ".*")], title='Save File As', initialdir='~')
    if text_file:
        name = text_file
        name = text_file.split("/")[len(text_file.split("/"))-1]
        file_name.config(text=name)
        window.title(f'{name} - fallenNotes')
  

def openfile(__init__):
    global filepath, nopath
    filepath = filedialog.askopenfilename(defaultextension='.txt', filetypes=[("Text file", ".txt"), ("All files", ".*")], title='Open File', initialdir='~')
    
    file_path = filepath
    nopath = file_path.split("/")[len(file_path.split("/"))-1]
    file_name.config(text=nopath)
    window.title(f'{nopath} - fallenNotes')
    filetext = open(filepath,'r')
    filething = filetext.read()
    text.delete('1.0', END)
    text.insert(END, filething)
    filetext.close()

def exitbutton(self):
    window.destroy()


def cut(self):
    global selected
    if self:
        selected = window.clipboard_get()
    else:
        if text.selection_get():
            selected = text.selection_get()
            text.delete("sel.first", "sel.last")
            window.clipboard_clear()
            window.clipboard_append(selected)


def copy(self):
    global selected
    if self:
        selected = window.clipboard_get()
    else:
        text.selection_get()
        selected = text.selection_get()
        window.clipboard_clear()
        window.clipboard_append(selected)


def paste(self):
    global selected
    if self:
        selected = window.clipboard_get()

    if selected:
        position = text.index(INSERT)
        text.insert(position, selected)

 
def select_all(event):
    text.tag_add(SEL, "1.0", END)
    text.mark_set(INSERT, "1.0")
    text.see(INSERT)


def bold(*args):
    boldfont = font.Font(text, text.cget("font"))
    boldfont.configure(weight="bold")

    current_tags = text.tag_names("sel.first")

    text.tag_configure("bold", font=boldfont)

    if "bold" in current_tags:
        text.tag_remove('bold', 'sel.first', 'sel.last')
    else:
        text.tag_add("bold", 'sel.first', 'sel.last')


def italics(*args):
    ifont = font.Font(text, text.cget("font"))
    ifont.configure(slant="italic")

    current_tags = text.tag_names("sel.first")

    text.tag_configure("ifont", font=ifont)

    if "ifont" in current_tags:
        text.tag_remove('ifont', 'sel.first', 'sel.last')
    else:
        text.tag_add("ifont", 'sel.first', 'sel.last')

def newfile(*args):
    text.delete('1.0', END)

window = Tk()
window.geometry("750x525")
window.title("fallenNotes")
icon = PhotoImage(file='fallenNotes.png')

logo = Label(window, text="fallenNotes", font=('Arial', 20, "bold"),
             bg='#E4E4E4', image=icon, compound="left")#, relief=RAISED, bd=10, padx=20, pady=20)
logo.pack()


yscrollbar = Scrollbar(window)
yscrollbar.pack(side=RIGHT, fill=Y)


window.iconphoto(True, icon)
menubar = Menu(window)


text = Text(window, font='Arial', yscrollcommand=yscrollbar.set, wrap=WORD, undo=True)
text.pack(expand=True, fill=BOTH)


yscrollbar.config(command=text.yview)


window.config(background='#E4E4E4', menu=menubar)

fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu,font=('Arial'))
fileMenu.add_command(label="New", font=('Arial', 10), command=lambda: newfile(False), accelerator="Ctrl+N")
fileMenu.add_command(label="Open", font=('Arial', 10), command=lambda: openfile(False), accelerator="Ctrl+O")
fileMenu.add_command(label="Save", font=('Arial', 10), command=lambda: save(False), accelerator="Ctrl+S")
fileMenu.add_command(label="Save As", font=('Arial', 10), command=lambda: saveas(False), accelerator="Alt+S")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", font=('Arial', 10), command=lambda: exitbutton(False), accelerator="Ctrl+Q")

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu,font=('Arial'))
editMenu.add_command(label="Undo", font=('Arial', 10), command=text.edit_undo, accelerator="Ctrl+Z")
editMenu.add_command(label="Redo", font=('Arial', 10), command=text.edit_redo, accelerator="Ctrl+Shift+Z")
editMenu.add_separator()
editMenu.add_command(label="Cut", font=('Arial', 10), command=lambda: cut(False), accelerator="Ctrl+X")
editMenu.add_command(label="Copy", font=('Arial', 10), command=lambda: copy(False), accelerator="Ctrl+C")
editMenu.add_command(label="Paste", font=('Arial', 10), command=lambda: paste(False), accelerator="Ctrl+V")
editMenu.add_separator()
editMenu.add_command(label="Select All", font=('Arial', 10), command=lambda: select_all(False), accelerator="Ctrl+A")


formatMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Format",menu=formatMenu,font=('Arial'))
formatMenu.add_command(label="Bold", font=('Arial', 10), command=lambda: bold(False))
formatMenu.add_command(label="Italics", font=('Arial', 10), command=italics)


file_name = Label(window, font='Arial', text='Ready   ', anchor=E)
file_name.pack(side=BOTTOM, fill=X, ipady=5)

window.bind('<Control-Key-q>', exitbutton)
window.bind('<Control-Key-Q>', exitbutton)
window.bind('<Control-Key-s>', save)
window.bind('<Control-Key-S>', save)
window.bind('<Control-Key-O>', openfile)
window.bind('<Control-Key-o>', openfile)
window.bind('<Control-Key-A>', select_all)
window.bind('<Control-Key-a>', select_all)
window.bind('<Alt-s>', saveas)


window.mainloop()