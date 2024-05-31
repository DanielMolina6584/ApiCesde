from domain.Crud import CRUD
from tabulate import tabulate

class Interaccion:
    def __init__(self):
        self.crud = CRUD()

    def crear_persona(self):
        nombre = input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        email = input("Ingrese el email: ")
        cel = input("Ingrese el número de celular: ")
        self.crud.crearInfoPersona(nombre, apellido, email, cel)

    def actualizar_persona(self):
        id_persona = input("Ingrese el ID de la persona a actualizar: ")
        nombre = input("Ingrese el nuevo nombre: ")
        apellido = input("Ingrese el nuevo apellido: ")
        email = input("Ingrese el nuevo email: ")
        cel = input("Ingrese el nuevo número de celular: ")
        self.crud.actualizarInfoPersona(id_persona, nombre, apellido, email, cel)

    def eliminar_persona(self):
        id_persona = input("Ingrese el ID de la persona a eliminar: ")
        self.crud.eliminarInfoPersona(id_persona)

    def ver_personas(self):
        print("Registros existentes:")
        registros = self.crud.getInfoPersona()
        if registros:
            headers = ["ID", "Nombre", "Apellido", "Email", "Celular"]
            tabla = [[registro[0], registro[1], registro[2], registro[3], registro[4]] for registro in registros]
            print(tabulate(tabla, headers=headers, tablefmt="grid"))
        else:
            print("No hay registros.")


    def ejecutar_acciones(self):
        while True:
            print("1. Crear persona")
            print("2. Actualizar persona")
            print("3. Eliminar persona")
            print("4. Ver personas")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_persona()
            elif opcion == "2":
                self.actualizar_persona()
            elif opcion == "3":
                self.eliminar_persona()
            elif opcion == "4":
                self.ver_personas()
            elif opcion == "5":
                print("Saliendo...")
                break
            else:
                print("Opción inválida.")


if __name__ == "__main__":
    interaction = Interaccion()
    interaction.ejecutar_acciones()
