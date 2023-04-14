import time


def writelines(file, lista):
    for linea in lista:
        file.write(linea+"\n")


res = []
with open("./Lezione0412/prova2.txt", "wt") as file: #apre il file in scrittura e lo chiude automaticamente quando non serve più
    i = 0
    while i == 4:
        i += 1
        file.write("ciao\nLuca")
        writelines(file, ["Ciao ancora", "Bella bionda"])
        time.sleep(3)#aspetta 3 secondi
        print(i)

with open("./Lezione0412/laboratorio.txt") as stream:#apre il file in lettura e lo chiude automaticamente quando non serve più
    L = []
    for item in stream:
        # spazio
        L = (item.strip()).split(":")#strip toglie gli spazi bianchi iniziali e finali, split divide la stringa in una lista di stringhe, ogni stringa è separata da uno spazio bianco
        spazio = L[0]#in posizione 0 c'è la stringa con lo spazio
        tempi = L[1]#in posizione 1 c'è la stringa con i tempi
        numeri = (tempi.strip()).split()#strip toglie gli spazi bianchi iniziali e finali, split divide la stringa in una lista di stringhe, ogni stringa è separata da uno spazio bianco
        media = 0
        for tempo in numeri:
            media += float(spazio)/float(tempo)
        media /= 4
        res.append(media)#aggiunge alla lista res il valore della media


def applica_a_tutti(lista, funzione):
    n_lista = []
    for x in lista:
        n_lista += [funzione(x)]#aggiunge alla lista n_lista il valore della funzione applicata a x
    return n_lista


with open("./Lezione0412/prova2.txt", "wt") as file:
    res = applica_a_tutti(res, str)
    # res = res.apply(str) #valida sula libreria numpy
    # res = [str(x) for x in res]
    stringa = " - ".join(res)
    print(stringa)

print("-"*20)#stampa 20 volte il carattere -