from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("\n===== RESTAURANTE APP =====")
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Registrar usuario")
    print("4. Listar usuarios")
    print("5. Vender producto")
    print("6. Consultar ventas de un usuario")
    print("7. Salir")


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- Registrar producto ---")

    codigo = input("Código: ")
    nombre = input("Nombre: ")
    categoria = input("Categoría: ")

    try:
        precio = float(input("Precio: "))
        stock = int(input("Stock: "))

        producto = Producto(
            codigo=codigo,
            nombre=nombre,
            categoria=categoria,
            precio=precio,
            stock=stock
        )

        if restaurante.registrar_producto(producto):
            print("Producto registrado correctamente.")
        else:
            print("Ya existe un producto con ese código.")

    except ValueError as error:
        print(f"Error: {error}")


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- Productos ---")

    productos = restaurante.listar_productos()

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print(producto)


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Registrar usuario ---")

    identificacion = input("Identificación: ")
    nombre = input("Nombre: ")
    correo = input("Correo: ")

    try:
        usuario = Usuario(
            identificacion=identificacion,
            nombre=nombre,
            correo=correo
        )

        if restaurante.registrar_usuario(usuario):
            print("Usuario registrado correctamente.")
        else:
            print("Ya existe un usuario con esa identificación.")

    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- Usuarios ---")

    usuarios = restaurante.listar_usuarios()

    if not usuarios:
        print("No hay usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)


def vender_producto(restaurante: Restaurante) -> None:
    print("\n--- Registrar venta ---")

    identificacion = input("Identificación del usuario: ")
    codigo = input("Código del producto: ")

    try:
        cantidad = int(input("Cantidad: "))

        usuario = restaurante.buscar_usuario(identificacion)
        producto = restaurante.buscar_producto(codigo)

        if usuario is None:
            print("El usuario no existe.")
            return

        if producto is None:
            print("El producto no existe.")
            return

        if cantidad <= 0:
            print("La cantidad debe ser mayor que cero.")
            return

        if producto.stock < cantidad:
            print(
                f"Stock insuficiente. "
                f"Stock disponible: {producto.stock}"
            )
            return

        if restaurante.vender_producto(codigo, identificacion, cantidad):
            print("Venta registrada correctamente.")
            print(f"Stock restante: {producto.stock}")
        else:
            print("No se pudo registrar la venta.")

    except ValueError:
        print("La cantidad debe ser un número entero.")


def consultar_ventas(restaurante: Restaurante) -> None:
    print("\n--- Ventas de un usuario ---")

    identificacion = input("Identificación del usuario: ")

    usuario = restaurante.buscar_usuario(identificacion)

    if usuario is None:
        print("El usuario no existe.")
        return

    ventas = restaurante.consultar_ventas_usuario(identificacion)

    if not ventas:
        print("El usuario no tiene ventas registradas.")
        return

    print(f"\nVentas de: {usuario.nombre}")

    for venta in ventas:
        producto = restaurante.buscar_producto(venta.producto_codigo)

        if producto is not None:
            print(
                f"Producto: {producto.nombre} | "
                f"Código: {producto.codigo} | "
                f"Cantidad: {venta.cantidad}"
            )
        else:
            print(
                f"Producto: {venta.producto_codigo} | "
                f"Cantidad: {venta.cantidad}"
            )


def main() -> None:
    restaurante = Restaurante()

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_producto(restaurante)

        elif opcion == "2":
            listar_productos(restaurante)

        elif opcion == "3":
            registrar_usuario(restaurante)

        elif opcion == "4":
            listar_usuarios(restaurante)

        elif opcion == "5":
            vender_producto(restaurante)

        elif opcion == "6":
            consultar_ventas(restaurante)

        elif opcion == "7":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()