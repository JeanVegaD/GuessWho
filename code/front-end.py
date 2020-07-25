from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk


def main_window():
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

    filedialog.askopenfilename(filetypes = (("Template files", "*.tplate")
                                                        ,("HTML files", "*.html;*.htm")
                                                        ,("All files", "*.*") ))

    #play bottom
    img_btn_play=Image.open("../src/images/play-button.png")
    img_resize_btn_play = img_btn_play.resize((70, 70), Image.ANTIALIAS)
    img_btn_play_aux = ImageTk.PhotoImage(img_resize_btn_play)
    btn_play=Button(main_window,bg="white",image=img_btn_play_aux,relief=FLAT,highlightthickness=0, bd=0).place(x=460,y=460)

    #info bottom
    img_btn_info=Image.open("../src/images/info.png")
    img_resize_btn_info = img_btn_info.resize((30, 30), Image.ANTIALIAS)
    img_btn_btn_info_aux = ImageTk.PhotoImage(img_resize_btn_info)
    btn_info=Button(main_window,bg="white",image=img_btn_btn_info_aux,relief=FLAT,highlightthickness=0, bd=0).place(x=730,y=500)    

    #help bottom
    img_btn_help=Image.open("../src/images/question.png")
    img_resize_img_btn_help = img_btn_help.resize((30, 30), Image.ANTIALIAS)
    img_btn_btn_help_aux = ImageTk.PhotoImage(img_resize_img_btn_help )
    btn_info=Button(main_window,bg="white",image=img_btn_btn_help_aux,relief=FLAT,highlightthickness=0, bd=0).place(x=690,y=500)    


    main_window.mainloop()


main_window()
