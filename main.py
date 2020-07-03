print("""
    Acciones disponibles:
        - registro
        - login
""")

from master_en_python.proyecto_python.usuarios import acciones

hazEl = acciones.Acciones()
accion = input("Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()