"""flask è a microservizio, è a single thread"""
"""è un linguaggio di scripting, è un piccolo programma per un unico utilizzo---per progetti medio-piccoli"""
"""è utilizzato nell'automotive, e funziona su ogni sistema operativo"""
"""è un linguaggio interpretato, viene quindi eseguito riga per riga"""
"""non ha un metodo main, inoltre le righe non finiscono con ;"""
"""il carattere di escape è \ e serve per stampare le cose dopo"""
#questo è un altro commento
#le funzioni sono equivalenti ai metodi statici in java, e deve essere dichiarata sopra il main, le espressioni all'interno delle funzioni devono essere indentate
#le funzioni sono dichiarate con def
#per creare un progetto ci basta creare una cartella e dentro mettere un file con estensione .py
#in python

#esempio di funzione
def funzione(parametro):
    print(parametro)
    return parametro

funzione("daniele ha gia vinto")

#vs java
#int funzione (int parametro){
#    return variabile;
#}

# il ** è l'elevamento a potenza
# per dare la precedenza alle operazioni, si usano le parentesi tonde
#il doppio slash è la divisione intera
#in python tutto è oggetto

#assegnamento : variabile = valore

#in python non c'è il ++ o il --, ma si può fare così: variabile += 1
#non si scrive il tipo di datto, perchè lo determina in automatico con l'assegnamento

x=None #viene inizializzata a null
print(x)

#in python di solito non si usa il camelcase, ma la best practice è usare il snake_case, a volte si usa anche l'underscore davanti alle variabili private
#i nomi non possono contenere $, %, #, @, !, & e non possono essere nessuna delle parole chiave del linguaggio

print("ciao" + "mirco")
print("#" * 3)
print("ciao", 5, "mirco") #qui viene aggiunto uno spazio tra le due stringhe

for i in range(99, 110, 2):#range è un oggetto che genera una sequenza di numeri, il primo è il valore di partenza, il secondo è il valore di arrivo, il terzo è il passo
    print(i)
#la funzione torna un oggetto che ci permette di iterare un loop for, per il decremento invece l'ultimo parametro è negativo

for fila in range (10):
    print(fila)

    stringa_fila = ""
    for posto in range(10):
        stringa_fila += "# "

    print(stringa_fila)
#l'indentazione è molto importante, le nuove righe devono essere allineate con la riga sopra per far capire che sono all'interno della stesso blocco di codice

txt = input()
numero = int(txt)#trasforma la stringa in numero
print(txt)#per leggere una cosa è sempre txt = input()