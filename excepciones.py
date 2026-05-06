class SoftwareFJException(Exception):
    pass

class ClienteInvalidoError(SoftwareFJException):
    pass

class ServicioNoDisponibleError(SoftwareFJException):
    pass

class ReservaError(SoftwareFJException):
    pass

class ValidacionError(SoftwareFJException):
    pass