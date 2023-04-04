def stampa_ripetuta(parola, numero=1, has_cornice=False): #se c'è un argomento opzionale deve essere messo per ultimo
    print(parola * numero)
    
stampa_ripetuta("mirco ")#è possibile utilizzare il polimorfismo, e quindi passare i il numero di argomenti
stampa_ripetuta("mirco ", has_cornice=True, numero=5)#se non specifico l'ordine devo rispettare l'ordine posizionale degli argomenti

import math  #importo tutte le funzioni di math
print(math.ceil(7.8568)) #arrotonda per eccesso, mi devo ricordare di mettere math prima della funzione se non ho importato tutto

def coppia():
    return "pippo", "pluto", "paperino", "minnie" #posso ritornare più valori, in questo caso due stringhe

a,b, *__= coppia() #posso assegnare più variabili alla volta, in questo caso a e b, con __* ignoro il resto dei valori, salti tutti i valori tranne il primo ritornato
print(b)

def visibilita():
    a="casa"
    
print(a)#non posso stampare a perchè è una variabile locale, non è visibile fuori dalla funzione

txt=input("ciao, inserisci il tuo nome: ")
print("quello che hai inserito è:", txt)

if txt=="mario rossi":#si possono anche omettere le parentesi tonde
   print("venuto")
elif txt=="gino paoli":
    print("malvenuto")
else:
    print("malvenuto")

# while txt != "luca verdi":#la struttura del while invece di usare la selezione effettua l'iterazione, i while con attenzione perchè possono creare un loop infinito
#     txt = input("utente non riconosciuto, inserisci il tuo nome: ")
    
if not ((5==5) and (4 < 9)):
    print("sei bravo in mate")

for lettera in "parola":
    print(lettera)#stampa ogni carattere uno dopo l'altro
    
a="caramella alla fragola"
#print(len(trova))
#stampare tutti gli indici in cui è presente la lettera a 

for i in range(len(a)): 
    if a[i]=="a":
        print(i)
        
print("\n")        
#in modo analogo si può fare utilzzando il find utilizzando il while


while a.find("a") != -1:
    i=a.find("a")
    print(a)
    
    a=a[i+1:]#a=a[i+1:] mi permette di continuare a cercare la lettera a a partire dall'indice successivo a quello trovato


    
