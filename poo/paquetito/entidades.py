class Vehiculo:
    # Metodo constructor
    def __init__(self, marca, modelo, color, velocidad, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = velocidad
        self.kilometraje = kilometraje
    # Metodos setter
    def setMarca(self, marca):
        self.marca = marca
    def setModelo(self, modelo):
        self.modelo = modelo
    def setColor(self, color):
        self.color = color
    def setVelocidad(self, velocidad):
        self.velocidad = velocidad
    def setKilometraje(self, kilometraje):
        self.kilometraje = kilometraje
    # Metodos getter
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getColor(self):
        return self.color
    def getVelocidad(self):
        return self.velocidad
    def getKilometraje(self):
        return self.kilometraje
    # Ah-doc (los que se requiera)
    def variarVelocidad(self, variacion):
        self.velocidad += variacion
    def variarKilometraje(self, variacion):
        self.kilometraje += variacion
    def imprimirDatos(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Color:", self.color)
        print("Velocidad:", self.velocidad, "Km/h")
        print("Kilometraje:", self.kilometraje, "Km")
        print()
