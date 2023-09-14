"""Escribe un programa en pseudocódigo que realize una búsqueda de un número dado, en un arreglo. 
   Crea una función modular para llevar a cabo la búsqueda."""

# Función para realizar la búsqueda de un número dentro del arreglo.
def BuscarNumero(arreglo, numero):
    for i in range (0, len(arreglo)): # Utilizamos un bucle "for" para recorrer cada elemento del arreglo. El rango va desde cero hasta la longitud el arreglo, que utiliza un "len".
        if arreglo[i] == numero_buscado: # Si se encuentra una coincidencia con el número ingresado, se ejecuta la condición if.
            return i # Se devuelve el índice donde se encuentra el número.
    return -1 # Si el bucle termina de recorrer todos los elementos del arreglo sin encontrar una coincidencia, se devuelve -1 para indicar que el número ingresado no existe dentro del arreglo.

arreglo = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20] # Definimos los elementos que debe contener el arreglo.
numero_buscado = int(input("Ingrese el número que desea buscar: ")) # Le pedimos al usuario que ingrese un número para comprobar si existe o no dentro del arreglo.
indice = BuscarNumero(arreglo, numero_buscado) # Llamamos a la función de buscar número. 

if indice != -1: # Si el número ingresado es diferente de -1 significa que existe dentro del arreglo y por lo tanto, se imprime el mensaje de su posición.
    print("El número", numero_buscado, "se encuentra en la posición n°", indice, "del arreglo.")
else: # De lo contrario, el número ingresado no existe dentro del arreglo.
    print("El número", numero_buscado, "no existe en el arreglo. Por favor ingrese otro número.")