class Fumetto:
    __titolo__ = "Fumetto" #attributo di classe
    
    def __init__(self, titolo, prezzo):
        self.titolo = titolo
        self.prezzo = prezzo
        self.Leggimi()
        
    def Leggimi(self):
        print("sono un fumetto")
        
    def __str__(self):
        return f"{self.titolo} - {self.prezzo}"
        
def Acquistami(self, quantita):
        prezzo =  quantita * 5
        print(prezzo)
        
def Leggimi(self):
        print(f"leggo il libro {self.titolo}")


Fumetto.Acquistami = Acquistami #aggiungo il metodo Acquistami alla classe Fumetto, le funzionalità necessitno del self perchè sono definite globalmente, ed il primo oggetto è il parametro della funzione
    
f = Fumetto("Manga", 3.99)
g = Fumetto("Lupo Alberto", 3.99)
f.Leggimi()

f.Acquistami(3)#stampa 3 * 5 = 15
# Acquistami(f, 3)

print(f)
print(g)
