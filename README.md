# Restaurante App - Semana 16

**Estudiante:** Anthony Sebastián Veloz Morales

## Descripción

Aplicación de escritorio desarrollada en Python utilizando Tkinter y programación orientada a objetos.

En la Semana 16 se continuó con la evolución del proyecto desarrollado en semanas anteriores, manteniendo las funciones de inicio de sesión, gestión de productos y registro de ventas.

En esta semana se incorporó la gestión de usuarios mediante operaciones CRUD, control de acceso según roles y manejo de diferentes eventos de Tkinter utilizando `command=` y `bind()`.

## Funcionalidades

La aplicación permite:

- Iniciar sesión.
- Gestionar productos.
- Registrar, consultar, actualizar y eliminar productos.
- Registrar ventas.
- Seleccionar usuarios y productos para una venta.
- Visualizar las ventas registradas.
- Gestionar usuarios mediante operaciones CRUD.
- Registrar nuevos usuarios.
- Seleccionar usuarios desde un Treeview.
- Actualizar usuarios registrados.
- Eliminar usuarios con confirmación.
- Asignar roles a los usuarios.
- Restringir la gestión de usuarios según el rol.
- Evitar que el administrador autenticado elimine su propia cuenta.
- Guardar la información en archivos JSON.
- Recuperar la información al volver a ejecutar el programa.
- Mostrar logo e íconos desde la carpeta `assets`.

## Roles de usuario

La aplicación utiliza tres roles:

- **Administrador:** tiene acceso a la gestión de usuarios.
- **Empleado:** puede ingresar al sistema, pero no tiene acceso a la gestión administrativa de usuarios.
- **Cliente:** puede ser registrado como usuario del sistema, pero no tiene acceso a la gestión administrativa de usuarios.

El control del rol permite restringir el acceso a determinadas funciones de la aplicación.

## Gestión de usuarios

La sección de usuarios permite realizar las operaciones principales de un CRUD:

- Registrar usuarios.
- Consultar usuarios.
- Actualizar usuarios.
- Eliminar usuarios.

Cada usuario contiene los siguientes datos:

- Identificación.
- Nombre.
- Correo.
- Usuario.
- Contraseña.
- Rol.

Los usuarios registrados se muestran mediante un `Treeview` con la identificación, nombre, usuario y rol.

La contraseña no se muestra directamente en la tabla.

## Manejo de eventos

Durante la Semana 16 se utilizaron eventos de Tkinter mediante `command=` y `bind()`.

### Eventos con `command=`

Los botones ejecutan funciones callback mediante `command=`.

Ejemplo:

```python
tk.Button(
    frame_botones,
    text="Registrar",
    command=self.registrar_usuario
)
```

De esta manera, al presionar el botón se ejecuta el método encargado de registrar al usuario.

### Evento `<<TreeviewSelect>>`

Se utiliza para detectar cuando se selecciona un usuario en el `Treeview`.

```python
self.tabla_usuarios.bind(
    "<<TreeviewSelect>>",
    self.evento_seleccionar_usuario
)
```

Cuando se selecciona una fila, se obtiene la identificación y se consulta el usuario mediante `RestauranteServicio` para cargar sus datos en el formulario.

### Evento `<Return>`

La tecla Enter permite registrar un usuario desde el formulario.

```python
self.entry_contrasena_usuario.bind(
    "<Return>",
    self.evento_enter_usuario
)
```

El callback reutiliza el método `registrar_usuario()`.

### Evento `<Escape>`

La tecla Escape permite limpiar el formulario y quitar la selección actual.

```python
self.ventana.bind(
    "<Escape>",
    self.evento_escape_usuario
)
```

### Evento `<<ComboboxSelected>>`

El formulario utiliza un `Combobox` para seleccionar el rol del usuario.

```python
self.combo_rol.bind(
    "<<ComboboxSelected>>",
    self.evento_cambio_rol
)
```

Los roles disponibles son:

- Administrador
- Empleado
- Cliente

## Callbacks

Los eventos de la interfaz se conectan con funciones callback.

Estas funciones reciben el evento cuando corresponde y reutilizan los métodos existentes de la aplicación, evitando duplicar la lógica del programa.

La lógica relacionada con los usuarios y la persistencia se mantiene en `RestauranteServicio` y `ArchivoServicio`.

## Persistencia de datos

La información se almacena en archivos JSON ubicados en la carpeta `datos`.

Los archivos utilizados son:

- `productos.json`
- `usuarios.json`
- `ventas.json`

El archivo `usuarios.json` almacena los datos de los usuarios, incluyendo su rol.

Los cambios realizados al registrar, actualizar o eliminar un usuario se guardan en el archivo JSON y permanecen disponibles después de cerrar y volver a ejecutar la aplicación.

## Estructura del proyecto

```text
restaurante_app/
│
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
│
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
│
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
│
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
│
├── assets/
│   ├── logo.png
│   └── iconos/
│       ├── productos.png
│       ├── usuarios.png
│       └── ventas.png
│
├── main.py
└── README.md
```

## Arquitectura

El proyecto mantiene una estructura modular.

- `modelos`: contiene las clases utilizadas para representar productos, usuarios y ventas.
- `servicios`: contiene la lógica de negocio y el manejo de la persistencia.
- `ui`: contiene las interfaces gráficas desarrolladas con Tkinter.
- `datos`: contiene los archivos JSON.
- `assets`: contiene el logo y los íconos utilizados en la interfaz.

La interfaz gráfica no modifica directamente los archivos JSON. Las operaciones se realizan mediante los servicios del proyecto.

## Ejecución

Para ejecutar la aplicación se debe abrir una terminal en la carpeta `restaurante_app` y ejecutar:

```bash
py main.py
```

La aplicación inicia mostrando la pantalla de inicio de sesión.

Después de validar las credenciales, se muestra el panel principal con las opciones disponibles según el rol del usuario.

## Semana 16

Durante esta semana se amplió el proyecto de la Semana 15 incorporando una gestión más completa de eventos en Tkinter.

Se implementaron eventos de botones mediante `command=`, eventos de teclado y selección mediante `bind()`, gestión CRUD de usuarios, roles y persistencia en `usuarios.json`, manteniendo las funcionalidades desarrolladas anteriormente.