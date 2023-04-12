stream = open("lezione0412/laboratorio.txt") #apre il file in lettura

l = []
for item in stream:
    i = item.find(":")
    spazio = item[0:i]
    item = item[i+2:]
    
    media = 0
    for j in range(4):
        i = item.find(" ")
        tempo = item[0:i]
        item = item[i+1:]

        media += float(spazio) / float(tempo)

    # calcolo velocità
    media /= 4

    print(media)
stream.close()
    
with open("lezione0412/laboratorio.txt") as stream:
    L = []
    for item in stream:
        L = item.strip().split(":") #strip toglie gli spazi iniziali e finali, split divide la stringa in una lista di stringhe, usando come separatore il carattere passato come parametro (in questo caso : )
        spazio = L[0] #prendo l'elemento 0 della lista
        tempi = L[1]  #prendo l'elemento 1 della lista

        numeri = tempi.strip().split() #strip toglie gli spazi iniziali e finali, split divide la stringa in una lista di stringhe, usando come separatore lo spazio
        
        media = 0
        for tempo in numeri:
            media += float(spazio) / float(tempo) #calcolo la velocità media

        res = [] 
        media /= 4
        res.append(media)
        print("res: ", res)
        with open ("res.txt" , "w") as file:
            #mi scorre tutti gli elementi
            res = [str(x)for x in res] #trasforma tutti gli elementi della lista in stringhe e li mette in una nuova lista che viene assegnata a res
            stringa = " - ".join(res) #qui concatenano tutti gli elementi della lista con il carattere passato come parametro
            print(stringa)
            

#stream.close()

#come aprire un file in python in maniera migliore
file = open("nuovo.txt", "w") #apre il file in scrittura, se esiste lo sovrascrive
file.write("ciao\n nuova linea")
file.writelines("ciao\n n\nuova linea")

lista = ["ciao", "nuova linea"]
def writelines(file, lista):
    for linea in lista:
        file.write(linea)
        file.write("\n")

file.close()
        
#in python c'è l'ereditarietà, il polimorfismo ma non l'incapsulamento

#i dizionari sono simili alle liste ma hanno chiavi e valori si usano le graffe
{'nome': 'mario', 'cognome': 'rossi'}