from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import os.path

#This class handles all the functions of the game GUI
class GameWindow:
    def __init__(self,char_list):
        self.char_list=char_list
        self.winVar =Tk()
        self.winVar.geometry("1010x750")
        self.winVar.title("Guess Who?")
        self.winVar.config(bg="white")
        self.winVar.resizable(False, False)
        #Background window
        background=Image.open("../src/images/background_game.png")
        background_aux = ImageTk.PhotoImage(background)
        #Label(self.winVar,image=background_aux).place(x=-2,y=-2)
        self.setCharacter()
        self.setCombobox()
        self.setEntry()
        self.setScrollFrame()
       
        self.winVar.mainloop()

    #
    def setScrollFrame(self):
        charactersFrame=Frame(self.winVar,relief=FLAT,bd=1,width=990,height=550,bg="white")
        charactersFrame.place(x=-2,y=-2)
        
        def frameBind(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            
        canvas=Canvas(charactersFrame)
        charactersFrame_aux=Frame(canvas,bg="white")
        myscrollbar=Scrollbar(charactersFrame,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set,width=990,height=550,bg="white")

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=charactersFrame_aux,anchor='nw')
        charactersFrame_aux.bind("<Configure>",frameBind)
        canvas.configure(scrollregion=canvas.bbox("all"))

        number_characters = 2
        gridX=0
        gridY=0
        
        #Set background label for characters
        character=Image.open("../src/images/label.png")
        character_resize = character.resize((110, 130), Image.ANTIALIAS)
        character_aux = ImageTk.PhotoImage(character_resize)
        for i in (self.char_list):
            Label(charactersFrame_aux,image=character_aux,bg="white",relief=FLAT).grid(row=gridY, column=gridX, padx=25, pady=10)
            gridX+=1
            if(gridX==7):
                gridX=0
                gridY+=1

        #set image for characters
        gridX=30
        gridY=15
        cont=0
        for character in  (self.char_list):
            character.setImage()
            img=character.getImage()
            Button(charactersFrame_aux,image=img,bg="white",relief=FLAT).place(x=gridX,y=gridY)
            gridX+=164
            cont+=1
            if(cont>6):
                cont=0
                gridX=30
                gridY+=154


        gridX=31
        gridY=119
        cont=0
        for character in  (self.char_list):
            name_char=tk.StringVar()
            name_char.set(character.getName())
            Label(charactersFrame_aux,textvariable=name_char,relief=FLAT,width=12,bg="#F2F2F2",fg="#0ECA9B",font=('Corbel',11,"bold")).place(x=gridX,y=gridY)
            gridX+=164
            cont+=1
            if(cont>6):
                cont=0
                gridX=30
                gridY+=154

        #Defaul
        Label(self.winVar,image=character_aux,bg="white",relief=FLAT).place(x=30,y=600)

        charactersFrame_aux.mainloop()
        
    

    def setCharacter(self):
        character=Image.open("../src/images/label.png")
        character_resize = character.resize((110, 130), Image.ANTIALIAS)
        character_aux = ImageTk.PhotoImage(character_resize)
        #Label(self.winVar,image=character_aux,bg="white",relief=FLAT).place(x=30,y=558)
        Label(self.winVar,text="your character",relief=FLAT,width=12,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=37,y=570)
        

    def setCombobox(self):
        Label(self.winVar,text="Label",relief=FLAT,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=180,y=570)
        combo1 = ttk.Combobox(self.winVar, width = 27,text="hola")
        combo1['values'] = (' January')
        combo1.place(x=180,y=600)

        Label(self.winVar,text="Label",relief=FLAT,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=380,y=570)
        combo2 = ttk.Combobox(self.winVar, width = 27,text="hola")
        combo2['values'] = (' January')
        combo2.place(x=380,y=600)

        Label(self.winVar,text="Label",relief=FLAT,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=580,y=570)
        combo3 = ttk.Combobox(self.winVar, width = 27,text="hola")
        combo3['values'] = (' January')
        combo3.place(x=580,y=600)


        btn_load_filetxt=tk.StringVar()
        btn_load_filetxt.set("Seleccione un archivo")
        Button(self.winVar,textvariable=btn_load_filetxt,width=65,bg="#f2f2f2",fg="#404040",font=('Corbel',12),relief=FLAT,highlightthickness=0, bd=0,anchor="w").place(x=180,y=635)

    def setEntry(self):
        Label(self.winVar,text="Label",relief=FLAT,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=180,y=670)
        combo3 = ttk.Combobox(self.winVar, width = 60,text="hola")
        combo3['values'] = (' January')
        combo3.place(x=180,y=700)

        btn_load_filetxt=tk.StringVar()
        btn_load_filetxt.set("Seleccione un archivo")
        Button(self.winVar,textvariable=btn_load_filetxt,width=20,bg="#f2f2f2",fg="#404040",font=('Corbel',12),relief=FLAT,highlightthickness=0, bd=0,anchor="w").place(x=580,y=695)