from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.platypus import Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet

usuarios = {}
producto = {
    1: {"nombre_producto": "Portatil", "precio_producto": 12000, "cantidad_producto": 10},
    2: {"nombre_producto": "Mouse", "precio_producto": 8000, "cantidad_producto": 15},
    3: {"nombre_producto": "Audifonos", "precio_producto": 15000, "cantidad_producto": 30},
    4: {"nombre_producto": "Pantalla", "precio_producto": 30000, "cantidad_producto": 8},
    5: {"nombre_producto": "Teclado", "precio_producto": 5000, "cantidad_producto": 25}
}
ventas = {}

# Credenciales para usuario y admin
credenciales = {
    "admin": {"email": "admin", "clave": "1234"},
    "cliente": {"email": "cliente", "clave": "123"}
}

def generarPDF(resultado_compra):
    filename = "compra_producto.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []

    styles = getSampleStyleSheet()
    style_title = styles["Title"]

    data = [['Nombre Producto', 'Cantidad', 'Total a Pagar']]
    for item in resultado_compra:
        data.append(item)

    tabla = Table(data)
    tabla.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), colors.gray),
                               ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                               ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                               ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                               ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                               ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                               ('GRID', (0, 0), (-1, -1), 1, colors.black)]))

    elements.append(Paragraph("Resultado de la compra:", style_title))
    elements.append(tabla)

    doc.build(elements)

    print(f"Se ha generado el archivo '{filename}'.")


# Funcion para iniciar sesion (valida cual usuario se esta registrando y si es correcto)
def iniciarSesion():
    email = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")

    if email == credenciales["admin"]["email"] and clave == credenciales["admin"]["clave"]:
        print("\nHablalo pira")
        return "admin"
    elif email == credenciales["cliente"]["email"] and clave == credenciales["cliente"]["clave"]:
        print("Que se dice psps")
        return "cliente"
    else:
        print("Usuario incorrecto")
        return None

# Usuario

# Funcion para registrar el usuario (Solo admin)
def registrarUsuario():
    idUser = int(input("Ingrese su cédula: "))
    nameUser = input("Ingrese su nombre: ")
    emailUser = input("Ingrese su email: ")
    clave = input("Ingrese su clave: ")

    usuarios[idUser] = {"name": nameUser, "email": emailUser, "clave": clave}
    print("Usuario registrado exitosamente")

def consultarUsuarios():
    print("\nProductos disponibles:")
    print(f"{'ID':<10}{'Nombre':<20}{'Precio':<10}{'Cantidad':<10}")
    for idUser, datos in usuarios.items():
        print(f"{idUser:<10}{datos['name']:<20}{datos['email']:<10}{datos['clave']:<10}")


# Ventas

# Funcion para registrar la venta (Solo admin)
def registrarVenta():
    idProducto = int(input("Ingrese el ID del producto: "))
    factura = input("Ingrese la factura: ")

    if idProducto in producto:
        print("Producto encontrado/n")
        print(f"Nombre: {producto[idProducto]['nombre_producto']}")
        print(f"Precio: {producto[idProducto]['precio_producto']}")
        print(f"Cantidad disponible: {producto[idProducto]['cantidad_producto']}")
    else:
        print("Producto no encontrado")

    ventas[factura] = {"id_producto": idProducto}
    print("Venta registrada exitosamente")

def comprarProducto():
    idProducto = int(input("Ingrese el ID del producto que desea comprar: "))
    cantidad = int(input("Ingrese la cantidad que desea comprar: "))

    resultado_compra = []

    if idProducto in producto:
        if producto[idProducto]['cantidad_producto'] >= cantidad:
            producto[idProducto]['cantidad_producto'] -= cantidad
            nombre_producto = producto[idProducto]['nombre_producto']
            total_pagar = producto[idProducto]['precio_producto'] * cantidad
            resultado_compra.append((nombre_producto, cantidad, total_pagar))
            print(f"Producto: {nombre_producto}")
            print(f"Total a pagar: {total_pagar}")
        else:
            print("Cantidad insuficiente del producto.")
    else:
        print("Producto no encontrado")

    generarPDF(resultado_compra)


#Productos

# Funcion para registrar el producto (Solo admin)
def registrarProducto():
    idProducto = int(input("Ingrese el ID del producto: "))
    nombreProducto = input("Ingrese el nombre del producto: ")
    precioProducto = input("Ingrese el precio del producto: ")
    cantidadProducto = input("Ingrese la cantidad del producto: ")

    producto[idProducto] = {"nombre_producto": nombreProducto, "precio_producto": precioProducto, "cantidad_producto": cantidadProducto}
    print("Producto registrado exitosamente")

# Función para consultar productos (Cliente y admin)
def consultarProductos():
    print("\nProductos disponibles:")
    print(f"{'ID':<10}{'Nombre':<20}{'Precio':<10}{'Cantidad':<10}")
    for idProducto, datos in producto.items():
        print(f"{idProducto:<10}{datos['nombre_producto']:<20}{datos['precio_producto']:<10}{datos['cantidad_producto']:<10}")


# Función para comprar producto (Cliente)

# Función para modificar el producto (Solo admin)
def modificarProducto():
    idProducto = int(input("Ingrese el ID del producto a modificar: "))

    if idProducto in producto:
        nombreProducto = input("Ingrese el nuevo nombre del producto: ")
        precioProducto = float(input("Ingrese el nuevo precio del producto: "))
        cantidadProducto = int(input("Ingrese la nueva cantidad del producto: "))

        producto[idProducto] = {"nombre_producto": nombreProducto, "precio_producto": precioProducto, "cantidad_producto": cantidadProducto}
        print("Producto modificado exitosamente.")
    else:
        print("Producto no encontrado.")


# Función para eliminar el producto (Solo admin)
def eliminarProducto():
    idProducto = int(input("Ingrese el ID del producto a eliminar: "))

    if idProducto in producto:
        del producto[idProducto]
        print("Producto eliminado exitosamente.")
    else:
        print("Producto no encontrado.")



# Menu para opciones como administrador
def menuAdmin():
    while True:
        print("\nMenú Administrador:")
        print("1. Registrar Usuario")
        print("2. Consultar Usuario")
        print("3. Registrar Producto")
        print("4. Consultar Productos")
        print("5. Modificar Productos")
        print("6. Eliminar Productos")
        print("7. Registrar Venta")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrarUsuario()
        elif opcion == "2":
            consultarUsuarios()
        elif opcion == "3":
            registrarProducto()
        elif opcion == "4":
            consultarProductos()
        elif opcion == "5":
            modificarProducto()
        elif opcion == "6":
            eliminarProducto()
        elif opcion == "7":
            registrarVenta()
        elif opcion == "8":
            print("Melo todo bien")
            break
        else:
            print("Opción no válida")


# Función para mostrar el menú del cliente
def menuCliente():
    while True:
        print("\nMenú Cliente:")
        print("1. Consultar Productos")
        print("2. Comprar Producto")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultarProductos()
        elif opcion == "2":
            comprarProducto()
        elif opcion == "3":
            print("No se demore en volver pa")
            break
        else:
            print("Opción no válida")

rol = iniciarSesion()
if rol == "admin":
    menuAdmin()
elif rol == "cliente":
    menuCliente()