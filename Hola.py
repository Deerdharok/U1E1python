
with open('prueba.txt') as p:
    for i, line in enumerate(p):
        if i==0:
            line1 = line
        elif i==2:
            line2= line
import re
line1 = line1.replace(']','').replace('[','').replace('\n','')
line1= line1.replace('"','').split(",")
line2= line2.split(" ")
ordenado=[""]*(len(line2))
for value in line2:
    index1= line1.index(value)
    ordenado[index1] = value
    

print(ordenado)