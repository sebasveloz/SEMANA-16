from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta
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

        self._ventas: list[Venta] = (
            self.archivo_servicio.cargar_ventas()
        )

    # -------------------------
    # USUARIOS - SEMANA 16
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

    def obtener_usuario_por_acceso(
        self,
        nombre_usuario: str,
        contrasena: str
    ) -> Usuario | None:
        for usuario in self._usuarios:
            if (
                usuario.usuario == nombre_usuario
                and usuario.contrasena == contrasena
            ):
                return usuario

        return None

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios

    def cantidad_usuarios(self) -> int:
        return len(self._usuarios)

    def buscar_usuario(
        self,
        identificacion: str
    ) -> Usuario | None:
        identificacion = identificacion.strip()

        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario

        return None

    def registrar_usuario(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        nombre_usuario: str,
        contrasena: str,
        rol: str
    ) -> Usuario:

        identificacion = identificacion.strip()
        nombre = nombre.strip()
        correo = correo.strip()
        nombre_usuario = nombre_usuario.strip()
        contrasena = contrasena.strip()
        rol = rol.strip()

        if self.buscar_usuario(identificacion) is not None:
            raise ValueError(
                "Ya existe un usuario con esa identificación."
            )

        for usuario in self._usuarios:
            if usuario.usuario == nombre_usuario:
                raise ValueError(
                    "El nombre de usuario ya está registrado."
                )

        usuario = Usuario(
            identificacion,
            nombre,
            correo,
            nombre_usuario,
            contrasena,
            rol
        )

        self._usuarios.append(usuario)

        self.archivo_servicio.guardar_usuarios(
            self._usuarios
        )

        return usuario

    def actualizar_usuario(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        nombre_usuario: str,
        contrasena: str,
        rol: str
    ) -> Usuario:

        usuario = self.buscar_usuario(identificacion)

        if usuario is None:
            raise ValueError(
                "No existe un usuario con esa identificación."
            )

        nombre = nombre.strip()
        correo = correo.strip()
        nombre_usuario = nombre_usuario.strip()
        contrasena = contrasena.strip()
        rol = rol.strip()

        if not nombre:
            raise ValueError(
                "El nombre es obligatorio."
            )

        if not correo:
            raise ValueError(
                "El correo es obligatorio."
            )

        if not nombre_usuario:
            raise ValueError(
                "El usuario es obligatorio."
            )

        if not contrasena:
            raise ValueError(
                "La contraseña es obligatoria."
            )

        if rol not in [
            "Administrador",
            "Empleado",
            "Cliente"
        ]:
            raise ValueError(
                "El rol seleccionado no es válido."
            )

        for otro_usuario in self._usuarios:
            if (
                otro_usuario.usuario == nombre_usuario
                and otro_usuario.identificacion != identificacion
            ):
                raise ValueError(
                    "El nombre de usuario ya está registrado."
                )

        usuario.nombre = nombre
        usuario.correo = correo
        usuario.usuario = nombre_usuario
        usuario.contrasena = contrasena
        usuario.rol = rol

        self.archivo_servicio.guardar_usuarios(
            self._usuarios
        )

        return usuario

    def eliminar_usuario(
        self,
        identificacion: str
    ) -> None:

        usuario = self.buscar_usuario(identificacion)

        if usuario is None:
            raise ValueError(
                "No existe un usuario con esa identificación."
            )

        self._usuarios.remove(usuario)

        self.archivo_servicio.guardar_usuarios(
            self._usuarios
        )

    # -------------------------
    # PRODUCTOS
    # -------------------------

    def listar_productos(self) -> list[Producto]:
        return self._productos

    def cantidad_productos(self) -> int:
        return len(self._productos)

    def buscar_producto(
        self,
        codigo: str
    ) -> Producto | None:

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

    def eliminar_producto(
        self,
        codigo: str
    ) -> None:

        producto = self.buscar_producto(codigo)

        if producto is None:
            raise ValueError(
                "No existe un producto con ese código."
            )

        self._productos.remove(producto)

        self.archivo_servicio.guardar_productos(
            self._productos
        )

    # -------------------------
    # VENTAS - SEMANA 15
    # -------------------------

    def listar_ventas(self) -> list[Venta]:
        return self._ventas

    def cantidad_ventas(self) -> int:
        return len(self._ventas)

    def registrar_venta(
        self,
        usuario: str,
        producto: str
    ) -> Venta:

        usuario = usuario.strip()
        producto = producto.strip()

        if not usuario:
            raise ValueError(
                "Debe seleccionar un usuario."
            )

        if not producto:
            raise ValueError(
                "Debe seleccionar un producto."
            )

        usuario_existe = False

        for item in self._usuarios:
            if item.nombre == usuario:
                usuario_existe = True
                break

        if not usuario_existe:
            raise ValueError(
                "El usuario seleccionado no existe."
            )

        producto_existe = False

        for item in self._productos:
            if item.nombre == producto:
                producto_existe = True
                break

        if not producto_existe:
            raise ValueError(
                "El producto seleccionado no existe."
            )

        venta = Venta(
            usuario=usuario,
            producto=producto
        )

        self._ventas.append(venta)

        self.archivo_servicio.guardar_ventas(
            self._ventas
        )

        return venta