#scrivere la classe Fraction che rappresenta numeri razionali come 1/2 e 3/4
#le frazioni dovrebbero sempre essere salvate in forma ridotta, ad esempio salvare 4/12 1/3 e 6/-9 come -2/3 e creare una funzione mcd per questo

#oggetti: numeratore, denominatore, segno
class Fraction:
    def init(self, numeratore, denominatore):
        self.numeratore = numeratore
        self.denominatore = denominatore
        self.semplifica()

        def semplifica(self):
            mcd = self.calcola_mcd()
            self.numeratore //= mcd
            self.denominatore //= mcd
            if self.denominatore < 0:
                self.numeratore *= -1
                self.denominatore *= -1

        def calcola_mcd(self):
            a = abs(self.numeratore)
            b = abs(self.denominatore)
            while b > 0:
                a, b = b, a % b
            return a

        def __str__(self):
            if self.numeratore == 0:
                return "0"
            elif self.denominatore == 1:
                return str(self.numeratore)
            else:
                return f"{self.numeratore}/{self.denominatore}"

        def __add__(self, other):
            numeratore = self.numeratore * other.denominatore + self.denominatore * other.numeratore
            denominatore = self.denominatore * other.denominatore
            return Fraction(numeratore, denominatore)

        def __mul__(self, other):
            numeratore = self.numeratore * other.numeratore
            denominatore = self.denominatore * other.denominatore
            return Fraction(numeratore, denominatore)

        def __eq__(self, other):
            return self.numeratore == other.numeratore and self.denominatore == other.denominatore

        def __lt__(self, other):
            return self.numeratore * other.denominatore < other.numeratore * self.denominatore
        
