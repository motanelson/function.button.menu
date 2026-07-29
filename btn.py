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
        ft=0
        tf=0
        for f in range(12):
            ff="empty"
            if f<len(self.runers):
                ff=self.runers[f]
            else:
                ff="f"+str(f)
            
            self.labels.append(tk.Button(root,text=ff,command=lambda idx=f: self.f(idx)).grid(column=ft, row=tf,ipadx=10,ipady=10))
            ft=ft+1
            if ft>2:
                ft=0
                tf=tf+1
       
    def f(self,value:str):
        if value>=len(self.runers):
            print("error")
        else:
            os.system(self.runers[value])
files="progman.txt"
f1=open(files,"r")
r=f1.read()
f1.close()        
r=r.split("\n")
runers=[]
for rr in r:
   rr=rr.strip()
   if rr!="":
       runers.append(rr)
root = tk.Tk()
mesme=mes(root,runers)
root.mainloop()