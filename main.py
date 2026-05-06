import datetime
from cliente import Cliente
from reserva_sala import ReservaSala
from alquiler_equipo import AlquilerEquipo
from asesoria import Asesoria
from reserva import Reserva
from logger import registrar_evento
import excepciones

def iniciar_sistema_integral():
    registrar_evento("=== SISTEMA DE GESTIÓN EMPRESARIAL 'NEXUS SOLUTIONS' INICIADO ===")
    
    casos_prueba = [
        {"tipo": "CLI", "data": ("Roberto Forlán", "98765432", "r.forlan@email.net")},
        {"tipo": "CLI", "data": ("Marta", "no-es-numero", "marta@web.org")}, # ERROR: Documento inválido
        {"tipo": "SALA", "data": (8, 0.15)}, # Éxito con impuesto personalizado
        {"tipo": "EQUIPO", "data": ("Estación de Trabajo", 0)}, # ERROR: Días en cero
        {"tipo": "ASE", "data": (12,)}, # Correcto
        {"tipo": "CLI", "data": ("", "11223344", "anonimo@mail.com")}, # ERROR: Nombre vacío
        {"tipo": "SALA", "data": (-1, 0.19)}, # ERROR: Tiempo negativo
        {"tipo": "EQUIPO", "data": ("Servidor Rack", 5)}, # Éxito
        {"tipo": "ASE", "data": (4,)}, # Correcto
        {"tipo": "CLI", "data": ("Lucía Méndez", "55667788", "lucia.m@cloud.com")} # Correcto
    ]

    for i, item in enumerate(casos_prueba, 1):
        print(f"Procesando registro {i}...")
        try:
            if item["tipo"] == "CLI":
                nuevo = Cliente(*item["data"])
                registrar_evento(f"REGISTRO {i}: Cliente '{item['data'][0]}' dado de alta.")
            
            elif item["tipo"] == "SALA":
                if item["data"][0] <= 0: raise excepciones.ServicioNoDisponibleError("Espacio no disponible para ese tiempo")
                obj = ReservaSala(item["data"][0])
                final = obj.calcular_costo(item["data"][1])
                registrar_evento(f"REGISTRO {i}: Sala reservada. Facturación: ${final}")

            elif item["tipo"] == "EQUIPO":
                if item["data"][1] <= 0:
                    try:
                        raise ValueError("La duración debe ser al menos de 24 horas")
                    except ValueError as base_err:
                        raise excepciones.OperacionNoPermitidaError("Inconsistencia en alquiler") from base_err
                
                obj = AlquilerEquipo(item["data"][1])
                registrar_evento(f"REGISTRO {i}: {item['data'][0]} despachado correctamente.")

            elif item["tipo"] == "ASE":
                obj = Asesoria(item["data"][0])
                registrar_evento(f"REGISTRO {i}: Consultoría técnica agendada.")

        except (ValueError, excepciones.ServicioNoDisponibleError, excepciones.OperacionNoPermitidaError) as err:
            registrar_evento(f"REGISTRO {i}: ALERTA DE SISTEMA -> {str(err)}")
            if err.__cause__:
                registrar_evento(f"   ORIGEN TÉCNICO: {err.__cause__}")
        
        except Exception as general:
            registrar_evento(f"REGISTRO {i}: FALLO NO IDENTIFICADO -> {str(general)}")
        
        else:
            print(f"Paso {i} finalizado con éxito.")
        
        finally:
            registrar_evento(f"REGISTRO {i}: Transacción cerrada.\n")

    registrar_evento("=== SIMULACIÓN COMPLETADA - ESTADO DEL NÚCLEO: ESTABLE ===")

if __name__ == "__main__":
    iniciar_sistema_integral()
