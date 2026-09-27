# Restaurante App - Semana 15

**Estudiante:** Anthony Sebastián Veloz Morales

## Descripción

Aplicación de escritorio desarrollada en Python utilizando Tkinter y programación orientada a objetos.

En la Semana 15 se implementó el manejo de eventos mediante `command=` y funciones callback, incorporando el registro de ventas al proyecto existente.

## Funcionalidades

La aplicación permite:

- Iniciar sesión.
- Consultar usuarios registrados.
- Registrar productos.
- Consultar productos.
- Actualizar productos.
- Eliminar productos.
- Registrar ventas.
- Seleccionar un usuario y un producto.
- Visualizar las ventas registradas.
- Guardar las ventas en un archivo JSON.
- Recuperar las ventas al volver a ejecutar el programa.
- Mostrar logo e íconos desde la carpeta `assets`.

## Manejo de eventos

Para registrar una venta se utiliza un botón de Tkinter conectado mediante `command=` a una función callback.

Ejemplo:

```python
tk.Button(
    frame_venta,
    text="Registrar venta",
    command=self.registrar_venta
)