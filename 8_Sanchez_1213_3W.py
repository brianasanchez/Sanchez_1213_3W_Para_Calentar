print(" ")#print imprime un espacio
print("Sanchez Perez Briana Sarahi, 1213, 3-w")
print(" ")#print imprime un espacio

def sPos(a,b):#Define una función
    for i in range(len(a)):# Recorre la longitud de 'a'
        for j in range(len(b)):# Recorre la longitud de 'b'
            if(a[i] == b[j]):# Verifica si 'a' es igual a 'b'.
                return False# devuelve False
            else:# verifica ambas partes y si es falsa imprime false
                return True# devuelve True
            
print(sPos([10,9,8,7,6],[6,5,4,3,2,1]))#print imprime el resultado.
print(sPos([1,2,3,4,5],[5,6,7,8,9,10]))#print imprime el resultado.

print(" ")#print imprime un espacio