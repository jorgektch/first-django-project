from .validaciones import *
from .entidades import *

def realiza_registro_vehiculo():
    marca = leer_texto("Marca: ")
    modelo = leer_texto("Modelo: ")
    color = leer_texto("Color: ")
    velocidad = leer_decimal("Velocidad: ")
    kilometraje = leer_decimal("Kilometraje: ")
    mivehiculo = Vehiculo(marca, modelo , color, velocidad, kilometraje)
    mivehiculo.imprimirDatos()

