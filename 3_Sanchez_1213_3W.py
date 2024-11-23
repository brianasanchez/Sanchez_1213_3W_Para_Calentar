print(" ")#print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3-w")
print(" ")#print imprime un espacio

def isnum(a):# Define una función
    try:
        int(a) # convertir 'a' en un entero
    except:# excepción 
        return False;#  devuelve False
    return True;# devuelve True.

def length(a): # Define una función
    i = 0  #  variable 'i'
    if not (isnum(a)):# Verifica si 'a' no es un número.
        for i in range(len(a)):# Recorre la longitud de 'a'.
            i = i + 1# Incrementa 'i'
    elif(isnum(a)): # Verifica si 'a' es un número.
        return(a) # si 'a' es un número lo devuelve
    return(i)# Devuelve 'i'

print(length("holuuuu"))# Imprime la longitud de la cadena
print(length(["23","45","67","56"]))# Imprime la longitud de la lista

print(" ")#print imprime un espacio
