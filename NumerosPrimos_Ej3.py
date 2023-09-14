"""Escribe un programa que encuentre y muestre todos los números primos dentro de un rango dado. 
   Utiliza una función modular para determinar si un número es primo."""

# Función para comprobar si un número es primo.
def determinar_si_es_primo(numero): 
    if numero <= 1: # Si el número es menor o igual a 1, devuelve Falso ya que no es número primo en ese caso. 
        return False
    for i in range(2, int(numero/2+1)): # Luego se utiliza un "for" para iterar desde 2 hasta la mitad del número más 1. Esto se hace para verificar si el número es divisible por algún valor en ese rango. 
        if numero % i == 0: 
            return False # Si encuentra un divisor, se devuelve Falso indicando que el número no es primo.
    return True # Si no encuentra ningún divisor se devuelve Verdadero indicando que si es primo.

# Pedimos al usuario que ingrese el rango dentro del cual, el usuario desea los números son primos. 
rango_minimo = int(input("Ingrese el rango mínimo: "))
rango_maximo = int(input("Ingrese el rango máximo: ")) # Prueba ingresando como inicio el número 1 y como fin el número 20.
print("Los números primos dentro del rango asignado son:")
for numero in range(rango_minimo, rango_maximo): # Recorremos el rango desde el número mínimo hasta el número máximo.
    if determinar_si_es_primo(numero): # Para cada número en el rango, llamamos a la función para verificar si es primo.
        print(numero) # Por último, se muestran en en pantalla.
    