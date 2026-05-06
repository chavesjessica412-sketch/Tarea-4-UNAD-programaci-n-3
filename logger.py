import datetime

def registrar_evento(mensaje):
    """Guarda eventos y errores en logs.txt con fecha y hora."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{timestamp}] {mensaje}\n")
