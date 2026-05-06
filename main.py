import tkinter as tk
from tkinter import ttk, messagebox
from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from logger import logger

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Software FJ - Sistema de Reservas")
        self.root.geometry("650x500")

        frame = ttk.Frame(root, padding=10)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="REGISTRO DE RESERVAS", font=("Arial", 16)).pack()

        ttk.Label(frame, text="Nombre Cliente").pack()
        self.nombre = ttk.Entry(frame)
        self.nombre.pack()

        ttk.Label(frame, text="Documento").pack()
        self.doc = ttk.Entry(frame)
        self.doc.pack()

        ttk.Label(frame, text="Correo").pack()
        self.correo = ttk.Entry(frame)
        self.correo.pack()

        ttk.Label(frame, text="Tipo de Servicio").pack()
        self.servicio = ttk.Combobox(frame, values=["Sala", "Alquiler Equipo", "Asesoría"])
        self.servicio.pack()

        ttk.Label(frame, text="Cantidad (días/horas)").pack()
        self.cantidad = ttk.Entry(frame)
        self.cantidad.pack()

        ttk.Label(frame, text="Equipo (solo alquiler)").pack()
        self.equipo = ttk.Combobox(frame, values=["Laptop", "Proyector", "Cámara"])
        self.equipo.pack()

        ttk.Button(frame, text="Crear Reserva", command=self.crear).pack(pady=10)

    def limpiar_campos(self):
        self.nombre.delete(0, tk.END)
        self.doc.delete(0, tk.END)
        self.correo.delete(0, tk.END)
        self.cantidad.delete(0, tk.END)
        self.servicio.set("")
        self.equipo.set("")

    def crear(self):
        try:
            cliente = Cliente(
                self.nombre.get(),
                self.doc.get(),
                self.correo.get()
            )

            tipo = self.servicio.get()
            cantidad = int(self.cantidad.get())

            if tipo == "Sala":
                servicio = ReservaSala(cantidad)
            elif tipo == "Alquiler Equipo":
                servicio = AlquilerEquipo(cantidad, self.equipo.get())
            elif tipo == "Asesoría":
                servicio = Asesoria(cantidad)
            else:
                raise Exception("Seleccione servicio")

            reserva = Reserva(cliente, servicio)
            reserva.confirmar()
            total = reserva.procesar()

            messagebox.showinfo("Éxito", f"Reserva creada\nTotal: {total}")

            self.limpiar_campos()

        except Exception as e:
            logger.log("ERROR", str(e))
            messagebox.showerror("Error", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
