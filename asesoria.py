from servicio import Servicio

class Asesoria(Servicio):
    def __init__(self, horas):
        super().__init__("Asesoría", 100000)
        self.horas = horas

    def calcular_costo(self):
        return self.precio_base * self.horas

    def descripcion(self):
        return f"Asesoría por {self.horas} horas"