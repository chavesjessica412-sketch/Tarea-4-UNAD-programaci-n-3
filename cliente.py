from excepciones import ClienteInvalidoError, ValidacionError
from logger import logger

class Cliente:
    def __init__(self, nombre, documento, correo):
        try:
            if not nombre or len(nombre) < 3:
                raise ValidacionError("Nombre inválido")
            if not documento or len(documento) < 5:
                raise ValidacionError("Documento inválido")
            if "@" not in correo:
                raise ValidacionError("Correo inválido")

            self.__nombre = nombre
            self.__documento = documento
            self.__correo = correo

            logger.log("INFO", f"Cliente creado: {nombre}")

        except Exception as e:
            logger.log("ERROR", str(e))
            raise ClienteInvalidoError(str(e))

    def get_nombre(self):
        return self.__nombre

    def get_documento(self):
        return self.__documento

    def get_correo(self):
        return self.__correo

    def __str__(self):
        return f"{self.__nombre} ({self.__documento})"