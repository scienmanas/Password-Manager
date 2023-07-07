from tkinter import *
FONT = ("Arial",10,"normal")
class Labels(Label):
    def __init__(self,**kw):
        super().__init__()
        self.config(text=kw.get("text"),font=FONT)
        self.grid(row=kw.get("row"),column=kw.get("column"))
        