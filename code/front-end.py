from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
import os.path

from GameWindow import GameWindow
from Character import Character


def mainWindow():
    global main_window
    main_window=Tk()
    main_window.geometry("1010x750")
    main_window.title("Guess Who?")
    main_window.config(bg="#ffffff")
    main_window.resizable(False, False)
    #Fondo de la ventana
    fondo=Image.open("../src/images/background.png")
    fondo_aux = ImageTk.PhotoImage(fondo)
    ins_fondo=Label(main_window,image=fondo_aux).place(x=-2,y=-2)
    
    global nicknname
    nicknname=StringVar()
    entry_nickname=Entry(main_window,textvariable=nicknname,width=40,relief=FLAT, bg="#F2F2F2",fg="#0ECA9B",font=('Corbel',12)).place(x=350,y=331)

    global init_game
    init_game=False
    #load file bottom
    global btn_load_filetxt
    btn_load_filetxt=tk.StringVar()
    btn_load_filetxt.set("Seleccione un archivo")
    btn_load_file=Button(main_window,textvariable=btn_load_filetxt,width=35,bg="#F2F2F2",fg="#0ECA9B",font=('Corbel',12),relief=FLAT,highlightthickness=0, bd=0,command=loadFile,anchor="w").place(x=350,y=399)

    #play bottom
    img_btn_play=Image.open("../src/images/play-button.png")
    img_resize_btn_play = img_btn_play.resize((70, 70), Image.ANTIALIAS)
    img_btn_play_aux = ImageTk.PhotoImage(img_resize_btn_play)
    btn_play=Button(main_window,bg="white",image=img_btn_play_aux,relief=FLAT,highlightthickness=0, bd=0,command=initGame).place(x=460,y=460)

    #info bottom
    img_btn_info=Image.open("../src/images/info.png")
    img_resize_btn_info = img_btn_info.resize((30, 30), Image.ANTIALIAS)
    img_btn_btn_info_aux = ImageTk.PhotoImage(img_resize_btn_info)
    btn_info=Button(main_window,bg="white",image=img_btn_btn_info_aux,relief=FLAT,highlightthickness=0, bd=0,command=infoWindow).place(x=730,y=500)    

    #help bottom
    img_btn_help=Image.open("../src/images/question.png")
    img_resize_img_btn_help = img_btn_help.resize((30, 30), Image.ANTIALIAS)
    img_btn_btn_help_aux = ImageTk.PhotoImage(img_resize_img_btn_help )
    btn_info=Button(main_window,bg="white",image=img_btn_btn_help_aux,relief=FLAT,highlightthickness=0, bd=0,command=helpWindow).place(x=690,y=500)    

    main_window.mainloop()


#Open the file explorer. Load and validate the selected file
def loadFile():
        global init_game
        init_game=False
        filepath= filedialog.askopenfilename(filetypes = (("JSON files", "*.json"),("All files", "*.*") ))
        
        if(filepath!=""):
            nombre_archivo, extension = os.path.splitext(filepath)
            if(extension==".json"):
                btn_load_filetxt.set(nombre_archivo)
                init_game=True
                backend.loadCharacters(filepath)
                print(init_game)
            else:
                messagebox.showerror(title="File error", message="The file must be a .json")



#Verify that everything is correct to start the game
def initGame():
    global init_game
    print(init_game)
    if(init_game):
        if(nicknname!=""):
            print("entre")
        else:
            messagebox.showerror(title="Nickname error", message="Nicknname cannot be empty")
    else:
        messagebox.showerror(title="File error", message="Select a valid file")


#Infomation window
def infoWindow():
    global info_window
    info_window=Toplevel()
    info_window.geometry("345x500")
    info_window.title("Info")
    info_window.config(bg="#ffffff")
    info_window.resizable(False, False)
    info_window.grab_set()

    #Fondo de la ventana
    fondo=Image.open("../src/images/background_about.png")
    fondo_aux = ImageTk.PhotoImage(fondo)
    ins_fondo=Label(info_window,image=fondo_aux).place(x=-2,y=-2)

    info_window.mainloop()

#Help window
def helpWindow():
    global help_window
    help_window=Toplevel()
    help_window.geometry("345x500")
    help_window.title("Help")
    help_window.config(bg="#ffffff")
    help_window.resizable(False, False)
    help_window.grab_set()

    #Fondo de la ventana
    fondo=Image.open("../src/images/background_help.png")
    fondo_aux = ImageTk.PhotoImage(fondo)
    ins_fondo=Label(help_window,image=fondo_aux).place(x=-2,y=-2)

    help_window.mainloop()

def newGame():


    character_list=[]
    #game_window = GameWindow(character_list,)

newGame()



