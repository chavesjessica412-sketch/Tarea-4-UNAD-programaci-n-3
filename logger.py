import datetime

def log(tipo, mensaje):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{timestamp}] {tipo}: {mensaje}\n")
