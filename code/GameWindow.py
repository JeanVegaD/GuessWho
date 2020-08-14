from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import os.path
import backend
import random

#This class handles all the functions of the game GUI
class GameWindow:
    def __init__(self,char_list,user_character,char_list_pc,pc_character,comobo_list1,name_list):

        self.char_list=char_list
        self.char_list_pc=char_list_pc


        self.features_counter = []
        self.features_values = []
        self.features_counter_pc = []
        self.features_values_pc = []
        self.deleted_features = []
        self.deleted_features_pc = []
        for character in char_list:
            for feature in character.features:
                if not feature in self.features_values:
                    self.features_values += [feature]
                    self.features_counter += [1]
                else:
                    index_feature = self.features_values.index(feature)
                    self.features_counter[index_feature] += 1

                    
        self.features_counter_pc = self.features_counter.copy()
        self.features_values_pc = self.features_values.copy()   




        global char_list2
        char_list2=char_list

        self.user_character= user_character
        self.pc_character=pc_character


        #print("---------------------------------")
        #print(self.pc_character.name)
        #print(self.user_character.name)
        #print("---------------------------------")
        self.name_list=name_list
        self.comobo_list1=comobo_list1

        self.winVar =Tk()
        self.winVar.geometry("1010x750")
        self.winVar.title("Guess Who?")
        self.winVar.config(bg="white")
        self.winVar.resizable(False, False)

        self.setCharacter()
        self.setCombobox()
        self.setEntry()
        self.setScrollFrame()

        self.initConsole()
        self.startGame()
        mainloop()



    ##
    ##E: Lista de los caracteres a traves del self
    ##S: Crea una segunda imagen utilizable para la interfaz 
    ##R: La ruta de la imagen debe ser válida
    ##
    def setScrollFrame(self):
        charactersFrame=Frame(self.winVar,relief=FLAT,bd=1,width=990,height=550,bg="white")
        charactersFrame.place(x=-2,y=-2)
        
        def frameBind(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            
        canvas=Canvas(charactersFrame)
        global charactersFrame_aux
        charactersFrame_aux=Frame(canvas,bg="white")
        myscrollbar=Scrollbar(charactersFrame,orient="vertical",command=canvas.yview)
        canvas.configure(yscrollcommand=myscrollbar.set,width=990,height=550,bg="white")

        myscrollbar.pack(side="right",fill="y")
        canvas.pack(side="left")
        canvas.create_window((0,0),window=charactersFrame_aux,anchor='nw')
        charactersFrame_aux.bind("<Configure>",frameBind)
        canvas.configure(scrollregion=canvas.bbox("all"))

        gridX=0
        gridY=0
        for i in (self.char_list):
            Label(charactersFrame_aux,image=self.charlbl_aux,bg="white",relief=FLAT).grid(row=gridY, column=gridX, padx=25, pady=10)
            gridX+=1
            if(gridX==6):
                gridX=0
                gridY+=1

        #set image for characters
        gridX=32
        gridY=15
        cont=0
        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        for character in  (self.char_list):
            #print(character.name)
            character.setImage()
            img=character.getImage()
            Label(charactersFrame_aux,image=img,bg="white",relief=FLAT,highlightthickness=0,bd=0).place(x=gridX,y=gridY)
            gridX+=164
            cont+=1
            if(cont == 6):
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
            if(cont  == 6):
                cont=0
                gridX=30
                gridY+=154

        #Defaul
       

        #charactersFrame_aux.mainloop()


    ##
    ##E: Lista de los caracteres a traves del self
    ##S: Recarga las imagenes de los personajes 
    ##R: 
    ##
    def reloadCharacters(self):
        gridX=32
        gridY=15
        cont=0
        for character in  (self.char_list):
            character.setImage()
            img=character.getImage()
            Label(charactersFrame_aux,image=img,bg="white",relief=FLAT,highlightthickness=0,bd=0).place(x=gridX,y=gridY)
            gridX+=164
            cont+=1
            if(cont == 6):
                cont=0
                gridX=32
                gridY+=154

    

    ##
    ##E: Obtiene el personaje del usario del self
    ##S: Muestra en el personaje del usuario en la interfaz
    ##R: 
    ##
    def setCharacter(self):
        #Set background label for characters
        charlbl=Image.open("../src/images/label.png")
        charlbl_resize = charlbl.resize((110, 130), Image.ANTIALIAS)
        self.charlbl_aux = ImageTk.PhotoImage(charlbl_resize)
        Label(self.winVar,text="Your character",relief=FLAT,width=12,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=37,y=570)
        Label(self.winVar,image=self.charlbl_aux,bg="white",relief=FLAT).place(x=30,y=600)

    
        self.user_character.setSelectedImageChar()
        Label(self.winVar,image=self.user_character.getImage_aux(),bg="white",relief=FLAT).place(x=35,y=605)

        name_char=tk.StringVar()
        name_char.set(self.user_character.getName())
        Label(self.winVar,textvariable=name_char,relief=FLAT,width=12,bg="#F2F2F2",fg="#0ECA9B",font=('Corbel',11,"bold")).place(x=35,y=708)


    ##
    ##E: Obtiene los valores mediante el self
    ##S: Estabelce los combobox y setea las funciones de llenado 
    ##R: 
    ##
    def setCombobox(self):

        def fillCombo(combo,lista):
            cache = list()
            for element in lista:
                cache.append(element)
            combo['values'] = cache

        Label(self.winVar,text="Property",relief=FLAT,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=180,y=610)
        global str_combo_property
        str_combo_property=StringVar()
        combo_property = ttk.Combobox(self.winVar, width = 27,text="Property",state="readonly",textvariable=str_combo_property)
        combo_property['values'] = ('')
        combo_property.place(x=180,y=640)

        fillCombo(combo_property,self.comobo_list1)

        Label(self.winVar,text="Adjective",relief=FLAT,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=380,y=610)
        global str_combo_adjective
        str_combo_adjective=StringVar()
        combo_adjective = ttk.Combobox(self.winVar, width = 27,text="Adjective",state="readonly", textvariable=str_combo_adjective)
        combo_adjective['values'] = ('')
        combo_adjective.place(x=380,y=640)

        Label(self.winVar,text="Value",relief=FLAT,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=580,y=610)
        global str_combo_value
        str_combo_value=StringVar()
        combo_value = ttk.Combobox(self.winVar, width = 27,text="Value",state="readonly", textvariable=str_combo_value)
        combo_value['values'] = ('')
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

        Button(self.winVar,text="Ask Question",width=20,bg="#f2f2f2",fg="#404040",font=('Corbel',12),command=self.askIA ,relief=FLAT,highlightthickness=0,bd=0).place(x=780,y=640)

    ##
    ##E: Obtiene los valores mediante el self
    ##S: Estabelce los combobox y setea las funciones de llenado 
    ##R: 
    ##
    def setEntry(self):

        def fillCombo(combo,lista):
            cache = list()
            for element in lista:
                cache.append(element)
            combo['values'] = cache
            combo.current(0)

        Label(self.winVar,text="Guess character",relief=FLAT,bg="white",fg="#A6A6A6",font=('Corbel',11,"bold")).place(x=180,y=670)
        self.str_comobo_guess=StringVar()
        comobo_guess = ttk.Combobox(self.winVar, width = 94,text="guess",state="readonly", textvariable=self.str_comobo_guess)
        comobo_guess['values'] = (' January')
        comobo_guess.place(x=180,y=700)

        fillCombo(comobo_guess,self.name_list)

        Button(self.winVar,text="Submit",width=20,bg="#f2f2f2",fg="#404040",command=self.guessCharacter,font=('Corbel',12),relief=FLAT,highlightthickness=0, bd=0).place(x=780,y=695)

    ##
    ##UI: genera un cuadro de dialogo con las preguntas
    ##
    def askQuestion(self,msg):
        return messagebox.askyesno(message=msg, title="Question")
    

    ##
    ##UI: ventana de mostrar informacion en consola
    ##  
    def initConsole(self):
        console_window=Toplevel()
        console_window.geometry("345x500")
        console_window.title("Console")
        console_window.config(bg="#ffffff")
        console_window.resizable(False, False)
        self.textConsole = Text(console_window, height = 50, width = 50)
        self.textConsole.config(state=DISABLED)    
               
        self.textConsole.pack() 
        #console_window.mainl)oop(


    ##
    ##E: Mensaje a mostrar
    ##S: Incluye en la consola de comandos el mesanje ingresado
    ##R: 
    ##
    def insertInConsole(self,msg):
        message=str(msg)+"\n\n"
        self.textConsole.configure(state='normal')
        self.textConsole.insert(tk.END, message) 
        self.textConsole.configure(state='disabled')

    ##
    ##E: 
    ##S: Define el turno inicial del juego
    ##
    def setFirst(self):
        self.turn=random.randint(0,2)


    ##
    ##E: Obtiene el turno actual 
    ##S: Cambio el turno al del otro jugador
    ##
    def changeTurn(self):
        if (self.turn==0):
            self.turn=1
            self.insertInConsole("**USER TURN**")
        else:
            self.turn=0
            self.insertInConsole("**PC TURN**")
            self.pcTurn()


    ##
    ##E: 
    ##S: Inicia todas las configuaciones del juego 
    ##
    def startGame(self):
        self.insertInConsole("Game started")
        self.setFirst()
        self.changeTurn()


     ##
    ##E: 
    ##S: Ejecuta la funcion de la IA param juagar
    ##
    def pcTurn(self):
        max_index = self.features_counter_pc.index(max(self.features_counter_pc))
        feature = self.features_values_pc[max_index]
        self.insertInConsole("feature:")
        self.insertInConsole(str(feature))
        self.insertInConsole("Matching Quantity")
        self.insertInConsole(str(max(self.features_counter_pc)))

        question = "Character: "+feature[0]+"  "+feature[1]+" "+feature[2]+"?"
        self.insertInConsole("Question:")
        self.insertInConsole(question)
        answer = self.askQuestion(question)

        self.insertInConsole("Answer:")
        self.insertInConsole(answer)

        found_character = None
        flag = False
        for character in self.char_list_pc:
            if answer:
                if self.features_counter_pc[max_index] == 1 and feature in character.features:
                    flag = True
                    found_character = character
                else:
                    if not feature in character.features:
                        for fea in character.features:
                            if not fea in self.deleted_features_pc:
                                index_feature = self.features_values_pc.index(fea)
                                self.features_counter_pc[index_feature]-= 1
                                if self.features_counter_pc[index_feature] == 0:
                                    self.features_values_pc.remove(fea)
                                    del self.features_counter_pc[index_feature]                     
                        self.char_list_pc.remove(character)
            else:
                if feature in character.features:
                    for fea in character.features:
                        if not fea in self.deleted_features_pc:
                            index_feature = self.features_values_pc.index(fea)
                            self.features_counter_pc[index_feature]-= 1
                            if self.features_counter_pc[index_feature] == 0:
                                self.features_values_pc.remove(fea)
                                del self.features_counter_pc[index_feature]       
                    self.char_list_pc.remove(character)
        if not flag:
            self.changeTurn()
            for i in self.features_values_pc:
                if feature[0] in i and feature[1] in i:            
                    self.deleted_features_pc+=[i]
                    del self.features_counter_pc[self.features_values_pc.index(i)]
                    self.features_values_pc.remove(i)
        if flag:
            messagebox.showinfo("LOST","PC WINS YOUR CHARACTER IS "+found_character.name)
            self.winVar.destroy()
        if len(self.char_list_pc) == 1:
            #print("Su caracter es:"+self.char_list_pc[0].name)
            messagebox.showinfo("LOST","PC WINS YOUR CHARACTER IS "+self.char_list_pc[0].name)
            self.winVar.destroy()


            
    ##
    ##E: Obtiene los valores de los comobox 
    ##S: Crea una pregunta la cual se envia a la IA para ser analizada
    ##
    def askIA(self):
        if(str_combo_property.get()!="" and str_combo_adjective.get()!="" and str_combo_value.get()!=""):
            feature=[str_combo_property.get(),str_combo_adjective.get(),str_combo_value.get()]              
            if feature in self.pc_character.features:                
                for character in self.char_list:
                    if not feature in character.features:
                        index_character = self.char_list.index(character)
                        char=self.char_list[index_character]
                        char.state = False
                        char.imagepath="../src/images/xicon.png"
                        self.char_list[index_character]=char
            else:
                for character in self.char_list:
                    if feature in character.features:
                        index_character = self.char_list.index(character)
                        char=self.char_list[index_character]
                        char.imagepath="../src/images/xicon.png"
                        char.state = False
                        self.char_list[index_character]=char               
            self.reloadCharacters()
            counter = 0
            for i in self.char_list:
                if i.state:
                    counter+=1
            if counter == 1:
                messagebox.showinfo("WIN","YOU WIN PC CHARACTER IS "+self.pc_character.name)
                self.winVar.destroy()
            else:
                self.changeTurn()
                
        else:
            messagebox.showerror(title="Empty field", message="Fields cannot be empty")

     ##
    ##E: Obtiene un valor del comobobox
    ##S: Determina si el persona seleccionado es el correcto
    ##
    def guessCharacter(self):
        if(self.str_comobo_guess.get()!=""):
            self.insertInConsole("the user tried to guess the character with: "+ self.str_comobo_guess.get())
            if(self.str_comobo_guess.get()==self.pc_character.getName()):
                 self.insertInConsole("successful character")
                 messagebox.showinfo(title="Successful", message="You guessed the character")
            else:
                 self.insertInConsole("wrong character")
                 messagebox.showerror(title="Fail", message="Wrong character")
                 self.changeTurn()
        else:
            messagebox.showerror(title="Empty field", message="this field cannot be empty")



