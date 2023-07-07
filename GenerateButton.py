from tkinter import *

class Generate(Button):
    
    def __init__(self,**kw):
        super().__init__()
        self.config(text=kw.get("value"))
        self.config(width=kw.get("width"))
        if kw.get("columnspan"):
            self.grid(row=kw.get("row"),column=kw.get("column"),columnspan=kw.get("columnspan"))
        else:
            self.grid(row=kw.get("row"),column=kw.get("column"))
             
            