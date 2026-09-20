import tkinter as tk
from tkinter import ttk, messagebox


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
            padx=20,
            pady=20
        )

        titulo = tk.Label(
            self.frame,
            text="PANEL PRINCIPAL - RESTAURANTE APP",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=(0, 15))

        # Contenedor de navegación
        frame_navegacion = tk.Frame(self.frame)
        frame_navegacion.pack(
            fill="x",
            pady=(0, 10)
        )

        tk.Button(
            frame_navegacion,
            text="Productos",
            width=18,
            command=self.mostrar_productos
        ).pack(side="left", padx=5)

        tk.Button(
            frame_navegacion,
            text="Usuarios",
            width=18,
            command=self.mostrar_usuarios
        ).pack(side="left", padx=5)

        tk.Button(
            frame_navegacion,
            text="Cerrar sesión",
            width=18,
            command=self.salir
        ).pack(side="right", padx=5)

        # Contenedor del formulario
        frame_formulario = tk.LabelFrame(
            self.frame,
            text="Gestión de productos",
            padx=15,
            pady=15
        )
        frame_formulario.pack(
            fill="x",
            pady=10
        )

        tk.Label(
            frame_formulario,
            text="Código:"
        ).grid(row=0, column=0, padx=5, pady=5, sticky="e")

        self.entry_codigo = tk.Entry(
            frame_formulario,
            width=25
        )
        self.entry_codigo.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        tk.Label(
            frame_formulario,
            text="Nombre:"
        ).grid(row=0, column=2, padx=5, pady=5, sticky="e")

        self.entry_nombre = tk.Entry(
            frame_formulario,
            width=25
        )
        self.entry_nombre.grid(
            row=0,
            column=3,
            padx=5,
            pady=5
        )

        tk.Label(
            frame_formulario,
            text="Categoría:"
        ).grid(row=1, column=0, padx=5, pady=5, sticky="e")

        self.entry_categoria = tk.Entry(
            frame_formulario,
            width=25
        )
        self.entry_categoria.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        tk.Label(
            frame_formulario,
            text="Precio:"
        ).grid(row=1, column=2, padx=5, pady=5, sticky="e")

        self.entry_precio = tk.Entry(
            frame_formulario,
            width=25
        )
        self.entry_precio.grid(
            row=1,
            column=3,
            padx=5,
            pady=5
        )

        tk.Label(
            frame_formulario,
            text="Stock:"
        ).grid(row=2, column=0, padx=5, pady=5, sticky="e")

        self.entry_stock = tk.Entry(
            frame_formulario,
            width=25
        )
        self.entry_stock.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        # Contenedor de botones
        frame_botones = tk.Frame(frame_formulario)
        frame_botones.grid(
            row=3,
            column=0,
            columnspan=4,
            pady=15
        )

        tk.Button(
            frame_botones,
            text="Registrar",
            width=15,
            command=self.registrar_producto
        ).pack(side="left", padx=5)

        tk.Button(
            frame_botones,
            text="Cargar / Consultar",
            width=18,
            command=self.cargar_producto
        ).pack(side="left", padx=5)

        tk.Button(
            frame_botones,
            text="Actualizar",
            width=15,
            command=self.actualizar_producto
        ).pack(side="left", padx=5)

        tk.Button(
            frame_botones,
            text="Eliminar",
            width=15,
            command=self.eliminar_producto
        ).pack(side="left", padx=5)

        tk.Button(
            frame_botones,
            text="Limpiar",
            width=15,
            command=self.limpiar_formulario
        ).pack(side="left", padx=5)

        # Contenedor de tabla
        frame_tabla = tk.LabelFrame(
            self.frame,
            text="Productos registrados",
            padx=10,
            pady=10
        )
        frame_tabla.pack(
            fill="both",
            expand=True,
            pady=10
        )

        columnas = (
            "codigo",
            "nombre",
            "categoria",
            "precio",
            "stock"
        )

        self.tabla_productos = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            height=10
        )

        self.tabla_productos.heading(
            "codigo",
            text="Código"
        )
        self.tabla_productos.heading(
            "nombre",
            text="Nombre"
        )
        self.tabla_productos.heading(
            "categoria",
            text="Categoría"
        )
        self.tabla_productos.heading(
            "precio",
            text="Precio"
        )
        self.tabla_productos.heading(
            "stock",
            text="Stock"
        )

        self.tabla_productos.column(
            "codigo",
            width=100
        )
        self.tabla_productos.column(
            "nombre",
            width=180
        )
        self.tabla_productos.column(
            "categoria",
            width=140
        )
        self.tabla_productos.column(
            "precio",
            width=100
        )
        self.tabla_productos.column(
            "stock",
            width=80
        )

        self.tabla_productos.pack(
            fill="both",
            expand=True
        )

        self.actualizar_tabla()

    def obtener_datos_formulario(self):
        codigo = self.entry_codigo.get().strip()
        nombre = self.entry_nombre.get().strip()
        categoria = self.entry_categoria.get().strip()

        if not codigo:
            raise ValueError("Ingrese el código.")

        if not nombre:
            raise ValueError("Ingrese el nombre.")

        try:
            precio = float(
                self.entry_precio.get().strip()
            )
        except ValueError:
            raise ValueError(
                "El precio debe ser un número válido."
            )

        try:
            stock = int(
                self.entry_stock.get().strip()
            )
        except ValueError:
            raise ValueError(
                "El stock debe ser un número entero."
            )

        return codigo, nombre, categoria, precio, stock

    def registrar_producto(self) -> None:
        try:
            datos = self.obtener_datos_formulario()

            self.restaurante_servicio.registrar_producto(
                *datos
            )

            messagebox.showinfo(
                "Producto",
                "Producto registrado correctamente."
            )

            self.actualizar_tabla()
            self.limpiar_formulario()

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def cargar_producto(self) -> None:
        codigo = self.entry_codigo.get().strip()

        if not codigo:
            messagebox.showwarning(
                "Consulta",
                "Ingrese el código del producto."
            )
            return

        producto = (
            self.restaurante_servicio.buscar_producto(
                codigo
            )
        )

        if producto is None:
            messagebox.showerror(
                "Consulta",
                "Producto no encontrado."
            )
            return

        self.entry_nombre.delete(0, tk.END)
        self.entry_nombre.insert(
            0,
            producto.nombre
        )

        self.entry_categoria.delete(0, tk.END)
        self.entry_categoria.insert(
            0,
            producto.categoria
        )

        self.entry_precio.delete(0, tk.END)
        self.entry_precio.insert(
            0,
            str(producto.precio)
        )

        self.entry_stock.delete(0, tk.END)
        self.entry_stock.insert(
            0,
            str(producto.stock)
        )

    def actualizar_producto(self) -> None:
        try:
            datos = self.obtener_datos_formulario()

            self.restaurante_servicio.actualizar_producto(
                *datos
            )

            messagebox.showinfo(
                "Producto",
                "Producto actualizado correctamente."
            )

            self.actualizar_tabla()
            self.limpiar_formulario()

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def eliminar_producto(self) -> None:
        codigo = self.entry_codigo.get().strip()

        if not codigo:
            messagebox.showwarning(
                "Eliminar",
                "Ingrese el código del producto."
            )
            return

        confirmar = messagebox.askyesno(
            "Eliminar producto",
            "¿Está seguro de eliminar este producto?"
        )

        if not confirmar:
            return

        try:
            self.restaurante_servicio.eliminar_producto(
                codigo
            )

            messagebox.showinfo(
                "Producto",
                "Producto eliminado correctamente."
            )

            self.actualizar_tabla()
            self.limpiar_formulario()

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    def actualizar_tabla(self) -> None:
        for item in self.tabla_productos.get_children():
            self.tabla_productos.delete(item)

        productos = (
            self.restaurante_servicio.listar_productos()
        )

        for producto in productos:
            self.tabla_productos.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:.2f}",
                    producto.stock
                )
            )

    def limpiar_formulario(self) -> None:
        self.entry_codigo.delete(0, tk.END)
        self.entry_nombre.delete(0, tk.END)
        self.entry_categoria.delete(0, tk.END)
        self.entry_precio.delete(0, tk.END)
        self.entry_stock.delete(0, tk.END)

        self.entry_codigo.focus()

    def mostrar_productos(self) -> None:
        self.actualizar_tabla()

        messagebox.showinfo(
            "Productos",
            "La lista de productos está actualizada."
        )

    def mostrar_usuarios(self) -> None:
        usuarios = (
            self.restaurante_servicio.listar_usuarios()
        )

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

    def salir(self) -> None:
        self.frame.destroy()
        self.cerrar_sesion()