#come si aprono i files:
stream = open("lezione0412/file.txt") #apre il file in lettura
linee = stream.readline()#legge una riga fino al \n  e poi sposta lo stream alla riga successiva, il file è un flusso di bytes, non si può puù tornare indietro, ma bisogna riaprire il file
print(stream)
stream.close()
################################################
stream = open("lezione0412/file.txt") #apre il file in scrittura, se esiste lo sovrascrive
linee= stream.read() #legge tutto il file
print(linee)
################################################
stream=open("lezione0412/file.txt")
linee=stream.readlines() #legge tutto il file e lo mette in una lista di stringhe
print(linee)

for L in linee:
    print(":")
    print(L[::-1])#accedo a tutti gli elementi della lista con :: -1 inverte le liste e inverte le stringhe
    
################################################
#l'ultimo modo è iterare lo stream

for item in stream:
    print(item)
stream.close()


