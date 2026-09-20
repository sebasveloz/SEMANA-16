# restaurante_app - Semana 14

## Estudiante

**Anthony Sebastián Veloz Morales**

## Descripción

`restaurante_app` es una aplicación desarrollada en Python aplicando Programación Orientada a Objetos, arquitectura modular e interfaz gráfica mediante Tkinter.

Durante la Semana 14 se evolucionó la interfaz gráfica desarrollada previamente, incorporando componentes y contenedores para mejorar la organización y experiencia del usuario.

La aplicación mantiene el inicio de sesión y la consulta de usuarios, e incorpora una sección de gestión de productos que permite registrar, consultar, actualizar y eliminar productos desde la interfaz gráfica.

## Objetivo de la Semana 14

El objetivo de esta actividad es aplicar correctamente componentes, contenedores y gestores de geometría de Tkinter/ttk, manteniendo la separación de responsabilidades entre modelos, servicios, interfaz y datos.

La lógica de negocio se mantiene dentro de `RestauranteServicio`, mientras que la persistencia de los productos se realiza mediante `ArchivoServicio` y el archivo `productos.json`.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Componentes principales

### Modelo Producto

Representa los productos registrados en el restaurante.

Cada producto contiene:

- Código.
- Nombre.
- Categoría.
- Precio.
- Stock.

El modelo también contiene validaciones para evitar precios o cantidades de stock negativas.

### Modelo Usuario

Representa los usuarios disponibles en la aplicación y contiene la información utilizada para realizar la validación del acceso al sistema.

### ArchivoServicio

Se encarga de trabajar con los archivos JSON.

Sus principales responsabilidades son:

- Cargar los productos desde `productos.json`.
- Cargar los usuarios desde `usuarios.json`.
- Guardar las modificaciones realizadas sobre los productos.

De esta manera, la interfaz gráfica no manipula directamente los archivos JSON.

### RestauranteServicio

Contiene las operaciones y validaciones relacionadas con el funcionamiento de la aplicación.

Entre sus funciones se encuentran:

- Validar el acceso de los usuarios.
- Listar usuarios.
- Listar productos.
- Buscar productos mediante su código.
- Registrar productos.
- Actualizar productos.
- Eliminar productos.
- Solicitar la persistencia de los cambios mediante `ArchivoServicio`.

### LoginView

Representa la pantalla inicial de acceso.

Permite ingresar usuario y contraseña y utiliza `RestauranteServicio` para comprobar las credenciales antes de permitir el acceso al panel principal.

### MainView

Representa la interfaz principal de la aplicación.

Durante la Semana 14 esta vista fue mejorada utilizando diferentes componentes y contenedores de Tkinter.

Desde esta interfaz es posible:

- Consultar los productos registrados.
- Consultar los usuarios registrados.
- Registrar nuevos productos.
- Cargar o consultar un producto mediante su código.
- Actualizar productos existentes.
- Eliminar productos.
- Limpiar el formulario.
- Cerrar sesión.

## Componentes y contenedores utilizados

Para organizar la interfaz se utilizaron componentes de Tkinter y ttk, entre ellos:

- `Frame`: organización de diferentes zonas de la interfaz.
- `LabelFrame`: agrupación del formulario y de la tabla de productos.
- `Label`: identificación de campos.
- `Entry`: ingreso de datos.
- `Button`: ejecución de las operaciones mediante `command=`.
- `ttk.Treeview`: presentación organizada de los productos registrados.

También se utilizaron los gestores de geometría `pack()` y `grid()` para distribuir correctamente los componentes dentro de sus respectivos contenedores.

## Gestión de productos

La sección de productos permite realizar las siguientes operaciones:

### Registrar

Permite ingresar un nuevo producto indicando código, nombre, categoría, precio y stock.

El sistema evita registrar dos productos con el mismo código.

### Cargar / Consultar

Permite buscar un producto mediante su código.

Cuando el producto existe, sus datos son cargados automáticamente en el formulario.

### Actualizar

Permite modificar la información de un producto existente y guardar los cambios realizados.

### Eliminar

Permite eliminar un producto registrado mediante su código.

Antes de realizar la eliminación, la interfaz solicita confirmación al usuario.

## Persistencia de datos

La aplicación utiliza archivos JSON para conservar la información.

```text
datos/productos.json
datos/usuarios.json
```

Los productos son cargados al iniciar la aplicación y las operaciones de registro, actualización y eliminación son almacenadas nuevamente en `productos.json`.

La lectura y escritura de los datos se realiza mediante `ArchivoServicio`.

Esto permite que los cambios permanezcan disponibles incluso después de cerrar y volver a ejecutar la aplicación.

## Flujo de la aplicación

```text
Inicio
   ↓
main.py
   ↓
LoginView
   ↓
Validación mediante RestauranteServicio
   ↓
MainView
   ↓
Gestión de productos
   ↓
Registrar | Consultar | Actualizar | Eliminar
   ↓
RestauranteServicio
   ↓
ArchivoServicio
   ↓
productos.json
   ↓
Actualización de la interfaz
```

## Mejoras realizadas en la Semana 14

Durante esta semana se realizaron las siguientes mejoras:

- Se mantuvo el sistema de inicio de sesión.
- Se mantuvo la consulta de usuarios.
- Se reorganizó la interfaz principal utilizando contenedores.
- Se incorporó un formulario para gestionar productos.
- Se agregó una tabla para visualizar los productos registrados.
- Se implementó el registro de productos.
- Se implementó la consulta de productos mediante código.
- Se implementó la actualización de productos.
- Se implementó la eliminación de productos.
- Se agregó persistencia para conservar los cambios en `productos.json`.
- Se mantuvo separada la interfaz de la lógica de negocio y del acceso a los archivos.

## Pruebas realizadas

Se realizaron las siguientes comprobaciones:

1. La aplicación inicia correctamente desde `main.py`.
2. La pantalla de inicio de sesión funciona correctamente.
3. Las credenciales válidas permiten ingresar al panel principal.
4. La consulta de usuarios continúa funcionando.
5. Los productos registrados aparecen en la tabla.
6. Se puede registrar un nuevo producto.
7. Se puede consultar un producto mediante su código.
8. Se puede actualizar la información de un producto.
9. Se puede eliminar un producto.
10. La tabla se actualiza después de las operaciones realizadas.
11. Los cambios realizados se guardan en `productos.json`.
12. Los productos permanecen guardados después de cerrar y volver a ejecutar la aplicación.

## Ejecución

Para ejecutar la aplicación se debe abrir una terminal dentro de la carpeta `restaurante_app` y utilizar:

```bash
py main.py
```

También puede ejecutarse desde Visual Studio Code utilizando un intérprete de Python correctamente configurado.

## Conclusión

Durante la Semana 14 se evolucionó `restaurante_app` mediante el uso de componentes y contenedores de Tkinter/ttk.

La interfaz permite gestionar productos mediante operaciones de registro, consulta, actualización y eliminación, manteniendo la persistencia mediante archivos JSON.

La arquitectura modular permite conservar separadas las responsabilidades de los modelos, servicios, datos e interfaz, facilitando el mantenimiento y futuras mejoras de la aplicación.