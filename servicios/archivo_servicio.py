import json
from pathlib import Path

from modelos.producto import Producto
from modelos.usuario import Usuario
from modelos.venta import Venta


class ArchivoServicio:
    def __init__(self, carpeta_datos: str = "datos") -> None:
        self.carpeta_datos = Path(carpeta_datos)
        self.carpeta_datos.mkdir(exist_ok=True)

        self.archivo_productos = self.carpeta_datos / "productos.json"
        self.archivo_usuarios = self.carpeta_datos / "usuarios.json"
        self.archivo_ventas = self.carpeta_datos / "ventas.json"

    def _guardar_json(self, archivo: Path, datos: list[dict]) -> None:
        try:
            with open(archivo, "w", encoding="utf-8") as file:
                json.dump(datos, file, ensure_ascii=False, indent=4)
        except PermissionError:
            print(f"Error: no hay permisos para escribir en {archivo}.")

    def _cargar_json(self, archivo: Path) -> list[dict]:
        try:
            with open(archivo, "r", encoding="utf-8") as file:
                return json.load(file)

        except FileNotFoundError:
            return []

        except json.JSONDecodeError:
            print(f"Error: el archivo {archivo} contiene JSON inválido.")
            return []

        except PermissionError:
            print(f"Error: no hay permisos para leer {archivo}.")
            return []

    def guardar_productos(self, productos: list[Producto]) -> None:
        datos = [producto.to_dict() for producto in productos]
        self._guardar_json(self.archivo_productos, datos)

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

            except KeyError as error:
                print(f"Error: falta la clave {error} en productos.json.")
            except ValueError as error:
                print(f"Error en los datos del producto: {error}")

        return productos

    def guardar_usuarios(self, usuarios: list[Usuario]) -> None:
        datos = [usuario.to_dict() for usuario in usuarios]
        self._guardar_json(self.archivo_usuarios, datos)

    def cargar_usuarios(self) -> list[Usuario]:
        datos = self._cargar_json(self.archivo_usuarios)
        usuarios = []

        for dato in datos:
            try:
                usuario = Usuario(
                    identificacion=dato["identificacion"],
                    nombre=dato["nombre"],
                    correo=dato["correo"]
                )
                usuarios.append(usuario)

            except KeyError as error:
                print(f"Error: falta la clave {error} en usuarios.json.")
            except ValueError as error:
                print(f"Error en los datos del usuario: {error}")

        return usuarios

    def guardar_ventas(self, ventas: list[Venta]) -> None:
        datos = [venta.convertir_a_diccionario() for venta in ventas]
        self._guardar_json(self.archivo_ventas, datos)

    def cargar_ventas(self) -> list[Venta]:
        datos = self._cargar_json(self.archivo_ventas)
        ventas = []

        for dato in datos:
            try:
                venta = Venta(
                    usuario_id=dato["usuario_id"],
                    producto_codigo=dato["producto_codigo"],
                    cantidad=int(dato["cantidad"])
                )
                ventas.append(venta)

            except KeyError as error:
                print(f"Error: falta la clave {error} en ventas.json.")
            except ValueError as error:
                print(f"Error en los datos de la venta: {error}")

        return ventas