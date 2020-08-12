from PIL import Image, ImageTk
import os.path

#this class stores all the information of the characters
class Character:
    
    """
    def __init__(self, name, gender, ethnicity, hair, image, state, mustache, beard, skinMole, hat, glasses):
        self.name = name
        self.gender = gender
        self.ethnicity = ethnicity
        self.hair = hair
        
        self.state = state
        self.mustache = mustache
        self.beard = beard
        self.skinMole = skinMole
        self.hat = hat
        self.glasses = glasses
    """

    def __init__(self, name, imagepath):
        self.name = name
        self.imagepath=imagepath
        self.image=""
    

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

    
