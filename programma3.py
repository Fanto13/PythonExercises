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