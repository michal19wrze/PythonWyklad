import math

suma = 0
a = input("Wektor 1: ")
b = input("Wektor 2: ")

if (len(a) != len(b)):
    print "ERROR"

for x in range (0, len(a)):
    suma = suma + a[x] * b[x]

print suma
