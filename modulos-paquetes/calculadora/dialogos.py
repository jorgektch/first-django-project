from .operaciones import *

def realizar_operaciones():
    a = float(input("Ingresa el numero a: "))
    b = float(input("Ingresa el numero b: "))
    print(f"a + b = ", sumar(a, b))
    print(f"a - b = ", restar(a, b))
    print(f"a * b = ", multiplicar(a, b))
    print(f"a / b = ", dividir(a, b))

def sumar_numeros():
    a = float(input("Ingresa el numero a: "))
    b = float(input("Ingresa el numero b: "))
    res = sumar(a, b)
    print(f"a + b = ", res)

def restar_numeros():
    a = float(input("Ingresa el numero a: "))
    b = float(input("Ingresa el numero b: "))
    res = restar(a, b)
    print(f"a - b = ", res)

def multiplicar_numeros():
    a = float(input("Ingresa el numero a: "))
    b = float(input("Ingresa el numero b: "))
    res = multiplicar(a, b)
    print(f"a * b = ", res)

def dividir_numeros():
    a = float(input("Ingresa el numero a: "))
    b = float(input("Ingresa el numero b: "))
    res = dividir(a, b)
    print(f"a / b = ", res)

# A partir del reto anterior crea un paquete que se llame retos
# que contenga modulos que correspondan a cada no de los subretos
# cada modulo debe contener los metodos necesarios
# Llamar desde un script de prueba a los metodos de dialogo