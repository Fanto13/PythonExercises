import numpy as np

a = np.array([1,2,3])
b = [1,2,3]
c = np.array([4,5,6])

print(a*5)
print(b*5)
print(a*c)
print(a+c)
print(a**c)

r = np.arange(10)
print(r[2:8:3])
print(r[::-1])

r[3:5]=99
print(r)

i = np.array([[1,2,3], [0,0,0] ,[3,2,1]])
print(len)
print()