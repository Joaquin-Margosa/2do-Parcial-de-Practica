"""Crea un programa que permita realizar las operaciones matemáticas básicas suma, resta, multiplicación y división. 
   Utiliza funciones modulares para cada operación."""

# Función Suma
def suma(a, b):
    return a + b

# Función Resta
def resta(a, b):
    return a - b

# Función Multiplicación
def multiplicacion(a, b):
    return a * b

# Función División
def division(a, b):
    if b != 0:
        return a / b
    else: # Si el segundo número no es distinto de cero, no se puede realizar la división.
        print("No se puede dividir entre cero.")


numero1 = int(input("Ingresa el primer número: ")) # Solicitamos que se ingresen dos números para hacer las operaciones.
numero2 = int(input("Ingresa el segundo número: "))

# Se imprimen los resultados de las cuatro operaciones básicas.
print("Resultado de la suma:", suma(numero1, numero2))
print("Resultado de la resta:", resta(numero1, numero2))
print("Resultado de la multiplicación:", multiplicacion(numero1, numero2))
print("Resultado de la división:", division(numero1, numero2))