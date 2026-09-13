# restaurante_app - Semana 13

## Estudiante

**Anthony Sebastian Veloz Morales**

## Descripción

El proyecto `restaurante_app` corresponde a una aplicación desarrollada en Python aplicando Programación Orientada a Objetos y una estructura modular.

En la Semana 13 se inicia la transición de la aplicación basada en consola hacia una interfaz gráfica de usuario utilizando Tkinter.

Para esta primera versión gráfica se trabaja principalmente con productos y usuarios. La aplicación permite iniciar sesión mediante un acceso simulado y posteriormente ingresar a un panel principal donde se puede consultar la información registrada.

## Objetivo de la Semana 13

El objetivo de esta actividad es comprender la integración de una interfaz gráfica dentro de una aplicación organizada por modelos, servicios, datos y vistas.

La aplicación mantiene separadas las responsabilidades de cada componente y utiliza una única ventana principal de Tkinter.

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

Representa los productos registrados en el restaurante. Contiene información como código, nombre, categoría, precio y stock.

### Modelo Usuario

Representa los usuarios utilizados por la aplicación. Contiene la información necesaria para mostrar los usuarios y realizar la simulación de acceso al sistema.

### ArchivoServicio

Se encarga de leer la información almacenada en los archivos JSON de productos y usuarios.

De esta manera, las vistas gráficas no acceden directamente a los archivos de datos.

### RestauranteServicio

Se encarga de trabajar con los productos y usuarios cargados por `ArchivoServicio`.

Entre sus funciones se encuentran:

- validar el acceso al sistema;
- listar productos;
- listar usuarios;
- consultar la cantidad de productos registrados;
- consultar la cantidad de usuarios registrados.

### LoginView

Representa la pantalla inicial de acceso creada con Tkinter.

Permite ingresar un usuario y una contraseña. También muestra mensajes cuando existen campos vacíos o cuando las credenciales ingresadas son incorrectas.

### MainView

Representa el panel principal de la aplicación.

Desde esta vista se puede:

- visualizar los productos registrados;
- visualizar los usuarios registrados;
- observar la opción de ventas como funcionalidad pendiente;
- cerrar sesión y regresar a la pantalla de acceso.

### main.py

Es el punto de entrada de la aplicación.

Se encarga de crear la ventana principal de Tkinter, preparar `RestauranteServicio` y controlar el cambio entre `LoginView` y `MainView`.

## Flujo de la aplicación

```text
Inicio
   ↓
main.py
   ↓
LoginView
   ↓
Validación de usuario y contraseña
   ↓
RestauranteServicio
   ↓
MainView
   ↓
Productos | Usuarios | Ventas (pendiente)
   ↓
Cerrar sesión
   ↓
LoginView
```

La aplicación utiliza una sola ventana principal durante todo el proceso.

## Datos JSON

La información utilizada por la aplicación se encuentra almacenada en:

```text
datos/productos.json
datos/usuarios.json
```

Los datos son cargados mediante `ArchivoServicio` y posteriormente utilizados por `RestauranteServicio`.

## Pruebas realizadas

Se realizaron las siguientes comprobaciones:

1. La aplicación inicia correctamente desde `main.py`.
2. Se muestra primero la pantalla de acceso.
3. Los campos permiten ingresar usuario y contraseña.
4. Los campos vacíos generan un mensaje de advertencia.
5. Las credenciales incorrectas generan un mensaje de error.
6. Las credenciales válidas permiten ingresar al panel principal.
7. La opción Productos muestra los productos registrados.
8. La opción Usuarios muestra los usuarios registrados.
9. La opción Ventas se encuentra identificada como funcionalidad pendiente.
10. La opción Cerrar sesión permite regresar al Login dentro de la misma ventana.

## Ejecución

Para ejecutar la aplicación se debe ingresar a la carpeta `restaurante_app` y utilizar:

```bash
py main.py
```

También puede ejecutarse desde Visual Studio Code utilizando el intérprete de Python configurado.

## Conclusión

Durante la Semana 13 se implementó una primera interfaz gráfica para `restaurante_app` utilizando Tkinter.

La aplicación fue organizada manteniendo separados los modelos, servicios, datos y vistas. Se implementó una pantalla de acceso y un panel principal para consultar productos y usuarios.

Esta estructura permite continuar incorporando nuevas funcionalidades gráficas en las siguientes semanas sin concentrar toda la lógica del sistema en un solo archivo.