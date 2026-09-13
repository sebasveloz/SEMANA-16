import tkinter as tk

from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


class RestauranteApp:
    def __init__(self) -> None:
        self.ventana = tk.Tk()
        self.ventana.title("Restaurante App")
        self.ventana.geometry("500x400")

        self.restaurante_servicio = RestauranteServicio()

        self.mostrar_login()

    def limpiar_ventana(self) -> None:
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def mostrar_login(self) -> None:
        self.limpiar_ventana()

        LoginView(
            self.ventana,
            self.restaurante_servicio,
            self.mostrar_main
        )

    def mostrar_main(self) -> None:
        self.limpiar_ventana()

        MainView(
            self.ventana,
            self.restaurante_servicio,
            self.mostrar_login
        )

    def ejecutar(self) -> None:
        self.ventana.mainloop()


if __name__ == "__main__":
    app = RestauranteApp()
    app.ejecutar()