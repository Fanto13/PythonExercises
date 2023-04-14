#devo stampare una cornicetta di cancelletti e al centro il numero che l'utente scrive raddoppiato, quindi abbiamo 9 colonne e 5 righe, senza if. quindi solo con cicli for

txt = input("inserisci un numero intero: ")#inserisci il numero da inserire
if not txt.isnumeric():#se il numero inserito non è un numero
    print("errore: devi inserire un numero intero")#stampa errore
    exit()#esce dal programma
numero = int(txt)#trasforma la stringa in numero

numero_da_inserire_al_centro = numero * 2
def linea():#definisco la funzione linea
    print("#"*9) #stampo la prima riga di 9 #


for i in range(2):#stampo le righe 2 e 3
    linea()
print("#"*4 + str(numero_da_inserire_al_centro) + "#"*4)#stampo la riga 4 con il numero al centro, devo però convertire il numero in stringa per poterlo concatenare con le stringhe
for i in range(2):#stampo le righe 4 e 5
    linea()

print("\n")

#oppure posso fare
print("#"*4 + str(numero_da_inserire_al_centro) + "#"*4)
print("####" + str(numero_da_inserire_al_centro) + "####")
print(f"#{5*2}###{numero_da_inserire_al_centro}{7*8}##")#f serve per stampare le variabili dentro le stringhe, senza doverle convertire in stringa
for i in range(2):
    linea()