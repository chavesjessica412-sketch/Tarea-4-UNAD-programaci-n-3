from servicio import Servicio

class AlquilerEquipo(Servicio):
    def __init__(self, dias):
        super().__init__("Alquiler de Equipo", 80000)
        self.dias = dias

    def calcular_costo(self, descuento=0):
        return (self.precio_base * self.dias) - descuento

    def descripcion(self):
        return f"Equipo por {self.dias} días"