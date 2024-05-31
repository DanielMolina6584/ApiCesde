from domain.Crud import CRUD
from domain.Interaccion import Interaccion


if __name__ == "__main__":
    crud = CRUD()

    interaction = Interaccion()
    interaction.ejecutar_acciones()

    crud.cerrar_conexion()