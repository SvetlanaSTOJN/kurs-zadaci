class Knjiga:
   def __init__(self,naslov,autor,godina_izdanja):
       self.naslov=naslov
       self.autor=autor
       self.godina=godina_izdanja
   def  prikazi_podatke(self):
       print(self.naslov,self.autor,self.godina)
       