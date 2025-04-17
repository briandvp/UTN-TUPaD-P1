import math

#exercise 1
def imprimir_hola_mundo():
    print("Hola Mundo!")
if __name__ == "__main__":
    imprimir_hola_mundo()
#exercise 2
def saludar_usuario(name):
    print(f"Hi, {name}!")

if __name__ == "__main__":
    user_name = input("Enter your name: ")
    saludar_usuario(user_name)
#exercise 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
#exercise 4

def calcular_area_circulo(radio_param):
    return math.pi * radio_param ** 2

def calcular_perimetro_circulo(radio_param):
    return 2 * math.pi * radio_param

if __name__ == "__main__":
    try:
        radio = float(input("Ingresa el radio del círculo: "))
        area = calcular_area_circulo(radio)
        perimetro = calcular_perimetro_circulo(radio)
        print(f"Área del círculo: {area:.2f}")
        print(f"Perímetro del círculo: {perimetro:.2f}")
    except ValueError:
        print("Error: Debes ingresar un número válido.")
#exercise 5
def segundos_a_horas(segundos_param):
    return segundos_param / 3600
if __name__ == "__main__":
    segundos = float(input("Ingrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos son equivalentes a {horas:.2f} horas.")
#exercise 6
def tabla_multiplicar(numero):
    for i in range(1,11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
if __name__ == "__main__":
    try:
        numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
        tabla_multiplicar(numero)
    except ValueError:
        print("Error: Debes ingresar un número entero.")
#exercise 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    
    return suma, resta, multiplicacion, division

a = 10
b = 5
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")
#exercise 8
def calcular_imc(peso_p, altura_a):
    return peso_p / (altura_a ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")
#exercise 9
def celsius_a_fahrenheit(celsius_temp):
    return (celsius_temp * 9/5) + 32

celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}°F")
#exercise 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(numero1, numero2, numero3)
print(f"El promedio es: {promedio:.2f}")