import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario


class ArchivoServicio:
    def __init__(self, carpeta_datos: str = "datos") -> None:
        self.carpeta_datos = Path(carpeta_datos)

        self.archivo_productos = self.carpeta_datos / "productos.json"
        self.archivo_usuarios = self.carpeta_datos / "usuarios.json"

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
                    contrasena=dato["contrasena"]
                )
                usuarios.append(usuario)

            except (KeyError, ValueError) as error:
                print(f"Error al cargar usuario: {error}")

        return usuarios

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