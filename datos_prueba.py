casos_simulacion = [
    {"tipo": "cliente", "params": ("Julian Alcaraz", "10987654", "julian@tech.co")},
    {"tipo": "cliente", "params": ("", "55443322", "error@tech.co")},           # Correcto: Nombre vacio
    {"tipo": "sala",    "params": (10, 0.19)},                                   # Correcto: Reserva larga
    {"tipo": "equipo",  "params": ("Cámara 4K", -5)},                         # Error: Días negativos
    {"tipo": "asesoria","params": (2,)},                                        # Correcto
    {"tipo": "cliente", "params": ("Marta Lopez", "DOC-INVALIDO", "marta@mail.com")}, # Error: Documento sin usar numeros
    {"tipo": "sala",    "params": (0, 0.19)},                                   # Error: 0 horas
    {"tipo": "equipo",  "params": ("Dron Pro", 3)},                             # Correcto
    {"tipo": "asesoria","params": (15,)},                                       # Correcto: Asesoría extensa
    {"tipo": "cliente", "params": ("Soporte Técnico", "99900011", "soporte@fj.com")} # Correcto
]
