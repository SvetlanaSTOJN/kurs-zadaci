class Racun:
    
    def __init__(self,vlasnik,stanje):
        global novo_stanje
        self.vlasnik=vlasnik
        self.stanje=stanje
        novo_stanje= stanje
        
    def uplati(self,iznos):
        global novo_stanje
        novo_stanje=novo_stanje+iznos
        return novo_stanje
    def podigni(self,iznos):
        global novo_stanje
        if novo_stanje>0:
            novo_stanje=novo_stanje-iznos
            return novo_stanje
        else:
            print('Nema novca')
    