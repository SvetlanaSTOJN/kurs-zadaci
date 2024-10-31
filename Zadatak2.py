#Zadatak: Maksimalni broj u listi
#Napiši funkciju max_broj(lista) koja prima listu brojeva i vraća najveći broj u toj listi.
def max_broj(lista):
    najveci_broj=max(lista)
    return najveci_broj

lista1=(1,2,3,4,5)
print(max_broj(lista1))

# Zadatak: Kreiranje klase Auto
#Kreiraj klasu Auto koja ima dva atributa: marka i boja. 
# Napiši metodu prikazi_info() koja ispisuje informacije o autu.
from Auto import Auto
boja_lista=['plava','crvena','crna']
marka_lista=['Opel','Ford','KIA']
auto=Auto(boja_lista,marka_lista)
print(f'Informacija o autu: marka  {auto.marka} boja {auto.boja}')

#Zadatak: Izračunaj prosečnu vrednost brojeva u listi
#Napiši funkciju prosek(lista) koja prima listu brojeva i vraća njihovu prosečnu vrednost.
from statistics import mean
def prosek(lista):
    prosecni_broj=mean(lista)
    return prosecni_broj
print (prosek(lista1))

#Zadatak: Brojanje samoglasnika
#Napiši funkciju broj_samoglasnika(tekst) koja prima string
# i vraća broj samoglasnika (a, e, i, o, u) u tom stringu.
def broj_samoglasnika(tekst):
    broj_slova=[x for x in tekst if x=='a' or x=='e' or x=='i' or x== 'u' or x=='o' in tekst]
    return len(broj_slova)
print(broj_samoglasnika('aeou'))

#Napiši funkciju zameni_reci(recenica, stara_rec, nova_rec) koja prima rečenicu
# i menja svako pojavljivanje stara_rec sa nova_rec.

def zameni_rec(recenica,stara_rec,nova_rec):
   nova_recenica=recenica.replace(stara_rec,nova_rec)
   return nova_recenica
print( zameni_rec('Jedan, dva, tri ','Jedan','dva'))

#6. Zadatak: Kvadrat svakog elementa u listi
# Napiši funkciju kvadrati(lista) koja prima listu brojeva
# i vraća novu listu sa kvadratima tih brojeva.
def kvadrati(lista):
    nova_lista=[x**2 for x in lista]
    return nova_lista
print(kvadrati(lista1))

#7. Zadatak: Klasa Proizvod
#Kreiraj klasu Proizvod koja ima atribute naziv, cena, i kolicina.
# Dodaj metodu ukupna_vrednost() koja vraća ukupnu vrednost proizvoda (cena * količina).
from Proizvod import Proizvod
ukupna_cena= Proizvod('cokolada',3,5)
print(f'ukupna cena {ukupna_cena.naziv} je {ukupna_cena.ukupna_vrednost()}')

#Zadatak: Klasa Racun
# Napiši klasu Racun koja ima atribute vlasnik i stanje.
# Dodaj metodu uplati(iznos) koja povećava stanje za dati iznos,
# i metodu podigni(iznos) koja smanjuje stanje, ali samo ako ima dovoljno novca na računu.
from Racun import Racun
novi_racun=Racun('Stefan',1000)

print(novi_racun.uplati(200),novi_racun.podigni(150))


#9. Zadatak: Klasa Knjiga
#Napiši klasu Knjiga koja ima atribute naslov, autor, i godina_izdanja.
# Dodaj metodu prikazi_podatke() koja ispisuje sve podatke o knjizi.
from Knjiga import Knjiga
knjiga=Knjiga('Alhemicar', "Paulo Koeljo",1988)
knjiga.prikazi_podatke()

