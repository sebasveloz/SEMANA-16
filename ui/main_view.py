import tkinter as tk
from tkinter import messagebox


class MainView:
    def __init__(
        self,
        ventana: tk.Tk,
        restaurante_servicio,
        cerrar_sesion
    ) -> None:
        self.ventana = ventana
        self.restaurante_servicio = restaurante_servicio
        self.cerrar_sesion = cerrar_sesion

        self.frame = tk.Frame(self.ventana)
        self.frame.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=30
        )

        titulo = tk.Label(
            self.frame,
            text="PANEL PRINCIPAL - RESTAURANTE APP",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        cantidad_productos = (
            self.restaurante_servicio.cantidad_productos()
        )

        cantidad_usuarios = (
            self.restaurante_servicio.cantidad_usuarios()
        )

        resumen = tk.Label(
            self.frame,
            text=(
                f"Productos registrados: {cantidad_productos}\n"
                f"Usuarios registrados: {cantidad_usuarios}"
            ),
            font=("Arial", 11)
        )
        resumen.pack(pady=10)

        boton_productos = tk.Button(
            self.frame,
            text="Ver productos",
            width=25,
            command=self.mostrar_productos
        )
        boton_productos.pack(pady=5)

        boton_usuarios = tk.Button(
            self.frame,
            text="Ver usuarios",
            width=25,
            command=self.mostrar_usuarios
        )
        boton_usuarios.pack(pady=5)

        boton_ventas = tk.Button(
            self.frame,
            text="Ventas (pendiente)",
            width=25,
            command=self.mostrar_ventas_pendientes
        )
        boton_ventas.pack(pady=5)

        boton_salir = tk.Button(
            self.frame,
            text="Cerrar sesión",
            width=25,
            command=self.salir
        )
        boton_salir.pack(pady=20)

    def mostrar_productos(self) -> None:
        productos = self.restaurante_servicio.listar_productos()

        if not productos:
            messagebox.showinfo(
                "Productos",
                "No existen productos registrados."
            )
            return

        texto = "\n\n".join(
            str(producto)
            for producto in productos
        )

        messagebox.showinfo(
            "Productos registrados",
            texto
        )

    def mostrar_usuarios(self) -> None:
        usuarios = self.restaurante_servicio.listar_usuarios()

        if not usuarios:
            messagebox.showinfo(
                "Usuarios",
                "No existen usuarios registrados."
            )
            return

        texto = "\n\n".join(
            str(usuario)
            for usuario in usuarios
        )

        messagebox.showinfo(
            "Usuarios registrados",
            texto
        )

    def mostrar_ventas_pendientes(self) -> None:
        messagebox.showinfo(
            "Ventas",
            "Esta funcionalidad se implementará posteriormente."
        )

    def salir(self) -> None:
        self.frame.destroy()
        self.cerrar_sesion()