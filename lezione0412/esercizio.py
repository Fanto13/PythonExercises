#scrivere la classe Fraction che rappresenta numeri razionali come 1/2 e 3/4
#le frazioni dovrebbero sempre essere salvate in forma ridotta, ad esempio salvare 4/12 1/3 e 6/-9 come -2/3 e creare una funzione mcd per questo

#oggetti: numeratore, denominatore, segno

import math
class Fraction:
    mcd = 1
    def __init__(self, numeratore, denominatore):
        if denominatore < 0:
            self.numeratore = -numeratore
            self.denominatore = -denominatore
        elif denominatore == 0:
            raise ValueError("Non è possibile dividere per 0")
        else:
            self.numeratore = numeratore
            self.denominatore = denominatore
        self.MCD()
    def MCD(self):
        mcd = math.gcd(self.numeratore, self.denominatore)
        print("il massimo comun denominatore è:", mcd)
        self.numeratore = int(self.numeratore/mcd)
        self.denominatore = int(self.denominatore/mcd)
    def __str__(self):
        if self.denominatore == 1:
            return (f"{self.numeratore}")
        else:
            return (f"{self.numeratore}/{self.denominatore}")
    def __mul__(self, other):
        numeratore = self.numeratore * other.numeratore
        denominatore = self.denominatore * other.denominatore
        
numeratore = int(input("Inserisci il numeratore: "))
denominatore = int(input("Inserisci il denominatore: "))
a = Fraction(numeratore, denominatore)
print("la frazione in forma ridotta è:",a)
