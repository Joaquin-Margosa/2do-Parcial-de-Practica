"""Crea un programa que permita convertir entre grados Celsius y grados Fahrenheit. 
   Crea dos funciones modulares: una para convertir de °C a °F y otra para convertir de °F a °C"""

# Funciones
def convertir_celsius_a_fahrenheit(temperatura): # Función para pasar de grados Celsius a Fahrenheit.
    resultado = (temperatura * 9/5) + 32 # Fórmula
    return resultado # Devolvemos el resultado al programa principal.

def convertir_fahrenheit_a_celsius(temperatura): # Función para pasar de grados Fahrenheit a Celsius.
    resultado = (temperatura - 32) * 5/9
    return resultado 

opcion= int(input("¿Qué conversión desea hacer?" "\n" "1.Celsius a Fahrenheit" "\n" "2. Fahrenheit a Celsius" "\n" "Elige una opción: " ))
if opcion == 1: # Si su elección es 1, el programa va a pedirle al usuario que ingrese la temperatura en grados Celsius para convertirla en grados Fahrenheit.
    temperatura = int(input("Ingrese la temperatura en grados Celsius: "))
    resultado = convertir_celsius_a_fahrenheit(temperatura)
    print("La temperatura convertida es de:", resultado, "°F")
elif opcion == 2: # Si es 2, va a convertir Fahrenheit en Celsius.
    temperatura = int(input("Ingrese la temperatura en grados Fahrenheit: "))
    resultado = convertir_fahrenheit_a_celsius(temperatura)
    print("La temperatura convertida es de:", resultado, "°C")
else:
    print("Error: solo puedes elegir las opciones 1 o 2.") # Mostrará un mensaje de error en caso de que la elección no sea 1 ni 2. 

# Dentro de las condiciones llamamos a sus respectivas funciones.