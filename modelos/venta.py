from datetime import datetime


class Venta:
    def __init__(self, usuario, producto, fecha=None):
        self.usuario = usuario
        self.producto = producto
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "usuario": self.usuario,
            "producto": self.producto,
            "fecha": self.fecha
        }

    @classmethod
    def from_dict(cls, datos):
        return cls(
            datos["usuario"],
            datos["producto"],
            datos["fecha"]
        )