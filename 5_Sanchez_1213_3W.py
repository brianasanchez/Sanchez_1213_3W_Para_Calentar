print(" ")#print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3-w")
print(" ")#print imprime un espacio

def suma(a):#Define una función
    total = 0 # dando valor a la variable 'total'
    for i in range(len(a)):# Recorre la longitud de 'a'
        total += a[i] # haciendo operacion
    return total # devuelve total

def mult(a):#Define una función
    total = 1# dando valor a la variable 'total'
    for i in range(len(a)):# Recorre la longitud de 'a'
        total *= a[i] # haciendo operacion
    return total # devuelve total

print(suma([1,3,5,7]))#print imprime el resultado.
print(mult([2,4,6,8]))#print imprime el resultado.

print(" ")#print imprime un espacio