class Pets:

    def __init__(self, PetName):

        self.PetName = PetName
    def show(self):

        print(f"PetName is {self.PetName}")

class Animals(Pets):

    def __init__(self,PetName, animals):
        super().__init__(PetName)
        self.animals = animals
    
    #def animaltype(self, type):
    def show(self):

        print(f"PetName is {self.PetName},Type of Animal is {self.animals}")

class Dogs(Animals):

    def __init__(self, PetName, animals,type,voice):
        super().__init__(PetName, animals)
        self.type = type
        self.voice = voice
    
    # def sound(self, voice):
    #     self.voice = voice

    def show(self):

        print(f"PetName is {self.PetName}, Type of Animal is {self.animals}, Breed of Animal is {self.type}, The sound that animal makes is {self.voice}")





# a = Pets("Ash")
# # a.show()

# b = Animals("Ash","Domestic")
# b.show()

c = Dogs("DD", "Domestic", "Dogs","Bark")
# c.sound(")
c.show()