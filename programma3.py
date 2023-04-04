s1 = "afragola"

print(s1)
print(len(s1))
print(s1[1])
print(s1[1:1])
print(s1[2:4])
print(s1[::-1])#ci permette di accedere a sottoporzioni di stringhe ed array, in questo caso stampa la stringa al contrario

L=[1,2,3,4,5,6,7,8,9,10]
print(L)
print([L[2]])

print(L[3:1:-1])

print([1,2] + [4,2])
L+=[568]      #aggiunge un elemento alla lista
L.append(568) #aggiunge un elemento alla lista
print(L)

L1=["1", 5, 8, "12"]
L2=[]
for x in L1:
   # L2.append(x*2)
    L2=L2+[x*2]
    
    print(L2)

for x in L1:
    if type(x)==type(1):
        L2.append(int(x)*2)
    else:
        L2.append(float(x)*2)
        
ord("A") #ritornna la posizione del carattere nella tabella ascii
print(ord("B"))

print(chr(68))#ritorna il caattere corrispondente alla posizione nella tabella ascii

for i in range(26):
    print("{i}=>{lettera}")
    
import random 
n=random.randint(10,100)
print(n)

random.random()

print(random.choice("parola"))
print(random.choice([31,37,43,47, "numero_primo", "primo", "numero"]))

#estrarre i gironi del mondiale da una lista di squadre
#il risultato deve essere ad esempio spagna-francia, argentina-germania, marocco-brasile, giappone-svizzera , due squadre non ripetute e in ordine casuale
squadre=["germania", "francia","spagna", "argentina", "marocco", "brasile", "svizzera", "giappone"]
estratte=[]
def estrai():
    global squadre, estratte #per poter usare le variabili globali dentro la funzione
    s=random.choice(squadre)
    while True:
        s=random.choice(squadre)
        if s not in estratte:
            estratte += [s]#aggiungo la squadra estratta alla lista delle squadre estratte
            return s
        
        
for i in range(len(squadre)//2):
    s1=estrai()
    s2=estrai()
    girone = chr(i+ord("A"))#chr converte un numero in carattere, ord converte un carattere in numero
    print(f"{girone}: {s1}-{s2}")#una f-string è una stringa che contiene delle variabili, che vengono stampate all'interno della stringa, senza doverle convertire in stringa
    
print("\n")
    
for j in range(len(squadre)//2):
    s1 = random.choice(squadre)
    squadre.remove(s1)
    
    s2=random.choice(squadre)
    squadre.remove(s2)
    
    girone = chr(j+ord("A")) #fa la lista delle lettere dell'alfabeto ad ogni iterazione
    print(f"{girone}: {s1}-{s2}")
    
#tuple come gli array, sono iterabilili e si potrà accedervi tramite indici. si scrivono tra parentesi tonde. in python è la cosa più vicina alla costante
#le tuple una volta create non possono essere modificate
#si usano per tornare i valori della funzioni e così abbiamo la garanzia che non venga aggiunto un nuovo oggetto
[1,2,3]
tupla=(1,2,3)
domanda=(1)*(5)
non_tupla=(1.5)

L3=[]
for x in tupla:
    L3.append(x)
L3[0]=10
print(L3)