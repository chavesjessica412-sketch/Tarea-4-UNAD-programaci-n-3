from servicio import Servicio

class ReservaSala(Servicio):
    def __init__(self, horas):
        super().__init__("Reserva de Sala", 50000)
        self.horas = horas

    def calcular_costo(self, impuesto=0.19):
        return (self.precio_base * self.horas) * (1 + impuesto)

    def descripcion(self):
        return f"Sala por {self.horas} horas"