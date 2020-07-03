import master_en_python.proyecto_python.usuarios.usuario as modelo
import master_en_python.proyecto_python.notas.acciones as acciones
class Acciones:
    def registro(self):
        print("\n Ok! Vamos a registrarte en el sistema!")
        nombre = input("Qual es tu nombre?: ")
        apellidos = input("Cuales son tus apellidos?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contrasena: ")

        usuario = modelo.Usuario(nombre,apellidos,email,password)
        registro = usuario.registrar()
        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre}, te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")

    def login(self):
        print("Vale! Identificate en el sistema!")
        try:
            email = input("Introduce tu email: ")
            password = input("Introduce tu contrasena: ")

            usuario = modelo.Usuario('','',email, password)
            login = usuario.identificar()
            if email == login[3]:
                print(f"\n Bienvenido {login[1]}, te has registrado en el sistema el {login[5]}")
                self.proximaAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorecto")

    def proximaAcciones(self, usuario):
        print("""
            Acciones disponible:
            - crear nota (comando crear)
            - mostrar tus notas (comando mostrar)
            - eliminar nota (comando eliminar)
            - salir (comando salir)
        """)
        accion = input("Que quieres hacer?: ")
        hazEl = acciones.Acciones()
        if accion == "crear":
            hazEl.crear(usuario)
            self.proximaAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximaAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borar(usuario)
            self.proximaAcciones(usuario)

        elif accion == "salir":
            print(f"\n Ok {usuario[1]}, hasta pronto!")
            exit()
