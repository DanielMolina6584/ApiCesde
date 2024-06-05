from domain.Crud import Crud
from domain.Interaccion import Interaccion


if __name__ == "__main__":
    crud = Crud()

    interaction = Interaccion()
    interaction.ejecutar_acciones()

    crud.cerrar_conexion()