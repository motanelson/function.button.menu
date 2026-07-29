import tkinter as tk
from tkinter import ttk
import copy

class mes:
    def __init__(self,root):
        self.root=root
        root.title("interface")
        root.geometry("640x480")
        self.labels=[]
        self.lab=[]
        for f in range(12):
            l=copy.copy("f"+str(copy.copy(f)))
            self.lab.append(l)
            self.labels.append(tk.Button(root,text="f"+str(f),command=lambda idx=f: self.f(idx)).pack(ipadx=10,ipady=10))
       
    def f(self,value:str):
        print(value)
         

root = tk.Tk()
mesme=mes(root)
root.mainloop()