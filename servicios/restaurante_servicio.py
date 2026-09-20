from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio


class RestauranteServicio:
    def __init__(self) -> None:
        self.archivo_servicio = ArchivoServicio()

        self._productos: list[Producto] = (
            self.archivo_servicio.cargar_productos()
        )

        self._usuarios: list[Usuario] = (
            self.archivo_servicio.cargar_usuarios()
        )

    # -------------------------
    # USUARIOS
    # -------------------------

    def validar_acceso(
        self,
        nombre_usuario: str,
        contrasena: str
    ) -> bool:
        for usuario in self._usuarios:
            if (
                usuario.usuario == nombre_usuario
                and usuario.contrasena == contrasena
            ):
                return True

        return False

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios

    def cantidad_usuarios(self) -> int:
        return len(self._usuarios)

    # -------------------------
    # PRODUCTOS
    # -------------------------

    def listar_productos(self) -> list[Producto]:
        return self._productos

    def cantidad_productos(self) -> int:
        return len(self._productos)

    def buscar_producto(self, codigo: str) -> Producto | None:
        codigo = codigo.strip()

        for producto in self._productos:
            if producto.codigo == codigo:
                return producto

        return None

    def registrar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> Producto:

        codigo = codigo.strip()
        nombre = nombre.strip()
        categoria = categoria.strip()

        if self.buscar_producto(codigo) is not None:
            raise ValueError(
                "Ya existe un producto con ese código."
            )

        producto = Producto(
            codigo,
            nombre,
            categoria,
            precio,
            stock
        )

        self._productos.append(producto)
        self.archivo_servicio.guardar_productos(
            self._productos
        )

        return producto

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int
    ) -> Producto:

        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError(
                "No existe un producto con ese código."
            )

        nombre = nombre.strip()
        categoria = categoria.strip()

        if not nombre:
            raise ValueError(
                "El nombre es obligatorio."
            )

        if precio < 0:
            raise ValueError(
                "El precio no puede ser negativo."
            )

        if stock < 0:
            raise ValueError(
                "El stock no puede ser negativo."
            )

        producto.nombre = nombre
        producto.categoria = categoria
        producto.precio = precio
        producto.stock = stock

        self.archivo_servicio.guardar_productos(
            self._productos
        )

        return producto

    def eliminar_producto(self, codigo: str) -> None:
        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError(
                "No existe un producto con ese código."
            )

        self._productos.remove(producto)

        self.archivo_servicio.guardar_productos(
            self._productos
        )