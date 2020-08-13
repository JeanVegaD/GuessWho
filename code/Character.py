from PIL import Image, ImageTk
import os.path

class Character:


    def __init__(self, name, imagepath,features, state):
        self.name = name
        self.imagepath=imagepath
        self.image=""
        self.features = features
        self.state = state
    

    def setImage(self):
        #make image 
        character=Image.open(self.imagepath)
        character_resize = character.resize((100, 98), Image.ANTIALIAS)
        character_aux = ImageTk.PhotoImage(character_resize)
        self.image=character_aux

    #Return image from path
    def getImage(self):
        return self.image

    #return name
    def getName(self):
        return self.name

    
