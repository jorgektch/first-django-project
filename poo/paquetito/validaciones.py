def es_entero(numero_str):
    if numero_str.isdigit() == True:
        return True
    else:
        return False

def es_decimal(numero_str):
    puntos = numero_str.count('.')
    if puntos <= 1:
        if numero_str.replace('.','').isdigit() == True:
            return True
        else:
            return False
    else:
        return False

def leer_texto(texto):
    entrada = ""
    while entrada == "":
        entrada = input(texto)
    return entrada

def leer_entero(texto):
    entrada = ""
    while es_entero(entrada) != True:
        entrada = input(texto)
    return int(entrada)

def leer_decimal(texto):
    entrada = ""
    while es_decimal(entrada) != True:
        entrada = input(texto)
    return float(entrada)