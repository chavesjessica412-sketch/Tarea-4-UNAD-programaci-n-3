from logger import logger

class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "PENDIENTE"

    def confirmar(self):
        self.estado = "CONFIRMADA"
        logger.log("INFO", f"Reserva confirmada para {self.cliente}")

    def cancelar(self):
        self.estado = "CANCELADA"
        logger.log("INFO", f"Reserva cancelada para {self.cliente}")

    def procesar(self):
        try:
            costo = self.servicio.calcular_costo()

            # obtener duración (horas o días)
            duracion = getattr(self.servicio, "horas", None)
            if duracion is None:
                duracion = getattr(self.servicio, "dias", None)

            detalle = self.servicio.descripcion()

            logger.log(
                "INFO",
                f"Reserva PROCESADA | Cliente: {self.cliente} | Servicio: {detalle} | Duración: {duracion} | Costo: {costo}"
            )

            return costo

        except Exception as e:
            logger.log("ERROR", str(e))
            raise