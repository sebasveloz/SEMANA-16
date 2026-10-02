import tkinter as tk
from tkinter import messagebox


class LoginView:
    def __init__(
        self,
        ventana: tk.Tk,
        restaurante_servicio,
        mostrar_main
    ) -> None:
        self.ventana = ventana
        self.restaurante_servicio = restaurante_servicio
        self.mostrar_main = mostrar_main

        self.frame = tk.Frame(self.ventana)
        self.frame.pack(
            fill="both",
            expand=True,
            padx=40,
            pady=40
        )

        titulo = tk.Label(
            self.frame,
            text="RESTAURANTE APP",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=20)

        tk.Label(
            self.frame,
            text="Usuario:"
        ).pack()

        self.entrada_usuario = tk.Entry(
            self.frame,
            width=30
        )
        self.entrada_usuario.pack(pady=5)

        tk.Label(
            self.frame,
            text="Contraseña:"
        ).pack()

        self.entrada_contrasena = tk.Entry(
            self.frame,
            width=30,
            show="*"
        )
        self.entrada_contrasena.pack(pady=5)

        boton_ingresar = tk.Button(
            self.frame,
            text="Ingresar",
            command=self.ingresar
        )
        boton_ingresar.pack(pady=20)

    def ingresar(self) -> None:
        usuario = self.entrada_usuario.get().strip()
        contrasena = self.entrada_contrasena.get().strip()

        if not usuario or not contrasena:
            messagebox.showwarning(
                "Campos vacíos",
                "Ingrese usuario y contraseña."
            )
            return

        usuario_autenticado = (
            self.restaurante_servicio.obtener_usuario_por_acceso(
                usuario,
                contrasena
            )
        )

        if usuario_autenticado is not None:
            self.frame.destroy()
            self.mostrar_main(usuario_autenticado)

        else:
            messagebox.showerror(
                "Acceso incorrecto",
                "Usuario o contraseña incorrectos."
            )