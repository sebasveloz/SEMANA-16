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

    def listar_productos(self) -> list[Producto]:
        return self._productos

    def listar_usuarios(self) -> list[Usuario]:
        return self._usuarios

    def cantidad_productos(self) -> int:
        return len(self._productos)

    def cantidad_usuarios(self) -> int:
        return len(self._usuarios)