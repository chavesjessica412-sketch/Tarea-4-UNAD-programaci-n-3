from cliente import Cliente
from logger import registrar_log  
from excepciones import DatosInvalidosError 

datos_prueba_clientes = [
    {"nombre": "Ana Pérez", "documento": "10203040", "email": "ana@correo.com"},  # Correcto
    {"nombre": "", "documento": "50607080", "email": "juan@correo.com"},          # Error: Nombre vacío
    {"nombre": "Carlos Gómez", "documento": "ABC-123", "email": "carlos@correo.com"}, # Error: Documento inválido
    {"nombre": "Laura Ruiz", "documento": "90807060", "email": "lauracorreo.com"},    # Error: Email sin @
    {"nombre": "Pedro Díaz", "documento": "11223344", "email": "pedro@correo.com"},   # Correcto
    {"nombre": "Sofía Castro", "documento": None, "email": "sofia@correo.com"}        # Error: le faltan datos
]

for datos in datos_prueba_clientes:
    try:
            nuevo_cliente = Cliente(
            nombre=datos["nombre"], 
            documento=datos["documento"], 
            email=datos["email"]
        )
        
    except ValueError as e:
        error_msg = f"Fallo al registrar cliente con doc {datos['documento']}"
        registrar_log(f"ERROR: {error_msg} - Detalle: {str(e)}")
        
                
    except Exception as e:
        registrar_log(f"ERROR CRÍTICO INESPERADO: {str(e)}")
        
    else:
        registrar_log(f"ÉXITO: Cliente '{nuevo_cliente.nombre}' registrado correctamente.")
        
    finally:
        registrar_log("INFO: Intento de operación de cliente finalizado.\n")

print(f"Proceso terminado. Se registraron {len(clientes_registrados)} clientes válidos.")
print("Revisa el archivo logs.txt para ver el registro completo.")
