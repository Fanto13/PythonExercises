# Scrivi un programma che legga le ore lavorate da due impiegati e scriva il totale e la media giornaliera (per impiegato) ed il totale di ore lavorate.

z = int(input("quanti giorni ha lavorato l'impiegato 1? "))
x = int(input("Inserisci le ore lavorate da impiegato 1: "))
u = int(input("quanti giorni ha lavorato l'impiegato 2? "))
y = int(input("Inserisci le ore lavorate da impiegato 2: "))

totale = x + y
media_giornaliera = totale / 2
print("l'impiegato 1 ha lavorato", x, "ore", "e la sua media giornaliera è", x / z "per giorno")
print("l'impiegato 2 ha lavorato", y, "ore", "e la sua media giornaliera è", y / u, "per giorno")4


