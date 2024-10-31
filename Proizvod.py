class Proizvod:
    def __init__(self,naziv,cena,kolicina):
        self.naziv=naziv
        self.cena=cena
        self.kolicina=kolicina
        
    def ukupna_vrednost(self):
        ukupna=self.kolicina*self.cena
        return ukupna