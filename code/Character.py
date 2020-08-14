from PIL import Image, ImageTk
import os.path

class Character:

    ##
    ##E: Recibe el nombre, la ruta de la imagen, las caracteristicas y un estado. 
    ##S: Crea un objeto de tipo Character 
    ##R: Debe de haber un archivo JSON cargado y un nickname valido
    ##
    def __init__(self, name, imagepath,features, state):
        self.name = name
        self.imagepath=imagepath
        self.image=""
        self.features = features
        self.state = state
    
    ##
    ##E: Path de la imagen
    ##S: Crea una imagen utilizable para la interfaz 
    ##R: La ruta de la imagen debe ser válida
    ##
    def setImage(self):
        #make image 
        character=Image.open(self.imagepath)
        character_resize = character.resize((100, 98), Image.ANTIALIAS)
        character_aux = ImageTk.PhotoImage(character_resize)
        self.image=character_aux

    ##
    ##E: Path de la imagen
    ##S: Crea una segunda imagen utilizable para la interfaz 
    ##R: La ruta de la imagen debe ser válida
    ##
    def setSelectedImageChar(self):
        character=Image.open(self.imagepath)
        character_resize = character.resize((100, 98), Image.ANTIALIAS)
        character_aux = ImageTk.PhotoImage(character_resize)
        self.image_aux=character_aux

    ##
    ##E: Objeto de la imagen creado
    ##S: Retorna el objeto de la imagen 
    ##R: El objeto debe ser creado previamente
    ##
    def getImage(self):
        return self.image

    ##
    ##E: Objeto de la imagen aux creado
    ##S: Retorna el objeto de la imagen aux
    ##R: El objeto aux debe ser creado previamente
    ##
    def getImage_aux(self):
         return self.image_aux

    ##
    ##E: 
    ##S: Retorna el nombre del personaje
    ##R: 
    ##
    def getName(self):
        return self.name

    
