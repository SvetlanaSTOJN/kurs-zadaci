import random
class Auto:
    # Kreiraj klasu Auto koja ima dva atributa: marka i boja.
    def __init__(self,marka,boja):
        
        self.marka=random.choice(marka)
        self.boja=random.choice(boja )

