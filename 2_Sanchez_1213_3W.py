print(" ")#print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3-w")
print(" ")#print imprime un espacio

def mayor3(a,b,c):# Define una función 
    if((a > b) and (a > c)):# Verifica si el valor de 'a' es mayor que el valor de 'b' y luego el valor de 'c'
        return a#  devuelve el valor de 'a'.
    if((b > a) and (b > c)):# Verifica si el valor de 'b' es mayor que el valor de 'a' y luego el valor de 'c'
        return b#  devuelve el valor de 'b'.
    if((c > a) and (c > b)):# Verifica si el valor de 'c' es mayor que el valor de 'a' y luego el valor de 'b'
        return c#  devuelve el valor de 'c'
print(mayor3(90,28,7))#print imprime el resultado.

print(" ")#print imprime un espacio