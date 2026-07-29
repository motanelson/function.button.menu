import tkinter as tk
from tkinter import ttk
import copy
import os

class mes:
    def __init__(self,root,runers:list):
        self.runers=runers
        self.root=root
        root.title("interface")
        root.geometry("640x480")
        self.labels=[]
        self.lab=[]
        for f in range(12):
            ff="empty"
            if f<len(self.runers):
                ff=self.runers[f]
            else:
                ff="f"+str(f)
            self.labels.append(tk.Button(root,text=ff,command=lambda idx=f: self.f(idx)).pack(ipadx=10,ipady=10))
       
    def f(self,value:str):
        if value>=len(self.runers):
            print("error")
        else:
            os.system(self.runers[value])
         
runers=["notepad.exe","explorer.exe","pbrush.exe","write.exe","word.exe","exel.exe","edge.exe"]
root = tk.Tk()
mesme=mes(root,runers)
root.mainloop()