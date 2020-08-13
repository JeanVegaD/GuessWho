from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import os.path
import backend

#This class handles all the functions of the game GUI
class GameWindow:
    def __init__(self,char_list,user_character,comobo_list1,name_list):
        self.char_list=char_list
        global char_list2
        char_list2=char_list
        self.user_character= user_character
        self.name_list=name_list
        self.comobo_list1=comobo_list1

        self.winVar =Tk()
        self.winVar.geometry("1010x750")
        self.winVar.title("Guess Who?")
        self.winVar.config(bg="white")
        self.winVar.resizable(False, False)
        #Background window
        #background=Image.open("../src/images/background_game.png")
        #background_aux = ImageTk.PhotoImage(background)
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
        for i in (self.char_list):
            Label(charactersFrame_aux,image=self.charlbl_aux,bg="white",relief=FLAT).grid(row=gridY, column=gridX, padx=25, pady=10)
            gridX+=1
            if(gridX==7):
                gridX=0
                gridY+=1

        #set image for characters
        gridX=32
        gridY=15
        cont=0
        for character in  (self.char_list):
            character.setImage()
            img=character.getImage()
            Button(charactersFrame_aux,image=img,bg="white",relief=FLAT,highlightthickness=0,bd=0).place(x=gridX,y=gridY)
            gridX+=164
            cont+=1
            if(cont>6):
                cont=0
                gridX=32
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
       

        charactersFrame_aux.mainloop()
        
    def setCharacter(self):
        #Set background label for characters
        charlbl=Image.open("../src/images/label.png")
        charlbl_resize = charlbl.resize((110, 130), Image.ANTIALIAS)
        self.charlbl_aux = ImageTk.PhotoImage(charlbl_resize)
        Label(self.winVar,text="Your character",relief=FLAT,width=12,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=37,y=570)
        Label(self.winVar,image=self.charlbl_aux,bg="white",relief=FLAT).place(x=30,y=600)

    
        self.user_character.setImage()
        Label(self.winVar,image=self.user_character.getImage(),bg="white",relief=FLAT).place(x=35,y=605)

        name_char=tk.StringVar()
        name_char.set(self.user_character.getName())
        Label(self.winVar,textvariable=name_char,relief=FLAT,width=12,bg="#F2F2F2",fg="#0ECA9B",font=('Corbel',11,"bold")).place(x=35,y=708)

    def setCombobox(self):

        def fillCombo(combo,lista):
            cache = list()
            for element in lista:
                cache.append(element)
            combo['values'] = cache

        Label(self.winVar,text="Property",relief=FLAT,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=180,y=610)
        str_combo_property=StringVar()
        combo_property = ttk.Combobox(self.winVar, width = 27,text="Property",state="readonly",textvariable=str_combo_property)
        combo_property['values'] = (' January')
        combo_property.place(x=180,y=640)

        fillCombo(combo_property,self.comobo_list1)

        Label(self.winVar,text="Adjective",relief=FLAT,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=380,y=610)
        str_combo_adjective=StringVar()
        combo_adjective = ttk.Combobox(self.winVar, width = 27,text="Adjective",state="readonly", textvariable=str_combo_adjective)
        combo_adjective['values'] = (' January')
        combo_adjective.place(x=380,y=640)

        Label(self.winVar,text="Value",relief=FLAT,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=580,y=610)
        str_combo_value=StringVar()
        combo_value = ttk.Combobox(self.winVar, width = 27,text="Value",state="readonly", textvariable=str_combo_value)
        combo_value['values'] = (' January')
        combo_value.place(x=580,y=640)



        def onChangecomboPropiety(self):
            elementas=backend.filterAttributes(char_list2,str_combo_property.get())
            fillCombo(combo_adjective,elementas)
            str_combo_adjective.set("")
            str_combo_value.set("")

            #combo_adjective.current(0)

        def onChangecomboadjective(self):
            elementas=backend.filterValues(char_list2,str_combo_property.get(),str_combo_adjective.get())
            fillCombo(combo_value,elementas)
            str_combo_value.set("")
            #combo_value.current(0)

        combo_property.bind('<<ComboboxSelected>>', onChangecomboPropiety) 
        combo_adjective.bind('<<ComboboxSelected>>', onChangecomboadjective) 

        Button(self.winVar,text="Ask Question",width=20,bg="#f2f2f2",fg="#404040",font=('Corbel',12),relief=FLAT,highlightthickness=0,bd=0).place(x=780,y=640)

    def setEntry(self):

        def fillCombo(combo,lista):
            cache = list()
            for element in lista:
                cache.append(element)
            combo['values'] = cache
            combo.current(0)

        Label(self.winVar,text="Guess character",relief=FLAT,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=180,y=670)
        comobo_guess = ttk.Combobox(self.winVar, width = 94,text="guess",state="readonly")
        comobo_guess['values'] = (' January')
        comobo_guess.place(x=180,y=700)

        fillCombo(comobo_guess,self.name_list)

        Button(self.winVar,text="Submit",width=20,bg="#f2f2f2",fg="#404040",font=('Corbel',12),relief=FLAT,highlightthickness=0, bd=0).place(x=780,y=695)