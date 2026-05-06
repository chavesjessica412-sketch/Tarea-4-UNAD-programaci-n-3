from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, precio_base):
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):
    def __init__(self, horas):
        super().__init__("Reserva Sala", 50000)
        self.horas = horas

    def calcular_costo(self, impuesto=0.19):
        return self.precio_base * self.horas * (1 + impuesto)

    def descripcion(self):
        return f"Sala por {self.horas} horas"


class AlquilerEquipo(Servicio):
    def __init__(self, dias, equipo):
        super().__init__("Alquiler Equipo", 80000)
        self.dias = dias
        self.equipo = equipo

    def calcular_costo(self, descuento=0):
        return (self.precio_base * self.dias) - descuento

    def descripcion(self):
        return f"Equipo: {self.equipo} por {self.dias} días"


class Asesoria(Servicio):
    def __init__(self, horas):
        super().__init__("Asesoría", 100000)
        self.horas = horas

    def calcular_costo(self):
        return self.precio_base * self.horas

    def descripcion(self):
        return f"Asesoría por {self.horas} horas"