import tkinter as tk

def function1():
    print("chaine 1 séléctionnée")

def function2():
    print("chaine 2 séléctionnée")

def function3():
    print("chaine 3 séléctionnée")

def function4():
    print("chaine 4 séléctionnée")

root = tk.Tk()

menubar = tk.Menu(root)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Chaine 1", command=function1)
filemenu.add_command(label="Chaine 2", command=function2)
filemenu.add_command(label="Chaine 3", command=function3)
filemenu.add_command(label="Chaine 4", command=function4)
menubar.add_cascade(label="Choix des chaines", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
