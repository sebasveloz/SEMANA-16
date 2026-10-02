import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    def __init__(self, carpeta_datos: str = "datos") -> None:
        self.carpeta_datos = Path(carpeta_datos)

        self.archivo_productos = self.carpeta_datos / "productos.json"
        self.archivo_usuarios = self.carpeta_datos / "usuarios.json"
        self.archivo_ventas = self.carpeta_datos / "ventas.json"

    def _cargar_json(self, archivo: Path) -> list[dict]:
        try:
            with open(archivo, "r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(
                f"Error: el archivo {archivo} contiene JSON inválido."
            )
            return []

    # -------------------------
    # PRODUCTOS
    # -------------------------

    def cargar_productos(self) -> list[Producto]:
        datos = self._cargar_json(self.archivo_productos)
        productos = []

        for dato in datos:
            try:
                producto = Producto(
                    codigo=dato["codigo"],
                    nombre=dato["nombre"],
                    categoria=dato["categoria"],
                    precio=float(dato["precio"]),
                    stock=int(dato["stock"])
                )
                productos.append(producto)

            except (KeyError, ValueError) as error:
                print(f"Error al cargar producto: {error}")

        return productos

    def guardar_productos(
        self,
        productos: list[Producto]
    ) -> None:
        datos = []

        for producto in productos:
            datos.append(producto.to_dict())

        self.carpeta_datos.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.archivo_productos,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                datos,
                file,
                ensure_ascii=False,
                indent=4
            )

    # -------------------------
    # USUARIOS - SEMANA 16
    # -------------------------

    def cargar_usuarios(self) -> list[Usuario]:
        datos = self._cargar_json(self.archivo_usuarios)
        usuarios = []

        for dato in datos:
            try:
                usuario = Usuario(
                    identificacion=dato["identificacion"],
                    nombre=dato["nombre"],
                    correo=dato["correo"],
                    usuario=dato["usuario"],
                    contrasena=dato["contrasena"],
                    rol=dato.get("rol", "Administrador")
                )

                usuarios.append(usuario)

            except (KeyError, ValueError) as error:
                print(f"Error al cargar usuario: {error}")

        return usuarios

    def guardar_usuarios(
        self,
        usuarios: list[Usuario]
    ) -> None:
        datos = []

        for usuario in usuarios:
            datos.append(usuario.to_dict())

        self.carpeta_datos.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.archivo_usuarios,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                datos,
                file,
                ensure_ascii=False,
                indent=4
            )

    # -------------------------
    # VENTAS - SEMANA 15
    # -------------------------

    def cargar_ventas(self) -> list[Venta]:
        datos = self._cargar_json(self.archivo_ventas)
        ventas = []

        for dato in datos:
            try:
                venta = Venta.from_dict(dato)
                ventas.append(venta)

            except (KeyError, ValueError) as error:
                print(f"Error al cargar venta: {error}")

        return ventas

    def guardar_ventas(
        self,
        ventas: list[Venta]
    ) -> None:
        datos = []

        for venta in ventas:
            datos.append(venta.to_dict())

        self.carpeta_datos.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.archivo_ventas,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                datos,
                file,
                ensure_ascii=False,
                indent=4
            )