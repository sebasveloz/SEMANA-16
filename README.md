# restaurante_app - Semana 11

## Estudiante

**Anthony Sebastian Veloz Morales**

## Descripción

El proyecto `restaurante_app` es una aplicación desarrollada en Python utilizando programación orientada a objetos y una organización modular.

En esta Semana 11 se amplió el sistema desarrollado anteriormente para incorporar el manejo de usuarios, productos con stock y ventas. La aplicación permite registrar productos y usuarios, realizar ventas, controlar el stock disponible y consultar las ventas realizadas por un usuario.

La información del sistema se conserva mediante archivos JSON, permitiendo recuperar los datos cuando el programa vuelve a ejecutarse.

## Estructura del proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md
```

## Responsabilidad de los componentes

### Producto

La clase `Producto` representa los productos disponibles en el restaurante.

Contiene los siguientes atributos:

* Código
* Nombre
* Categoría
* Precio
* Stock

Además, valida que el precio y el stock no sean negativos y permite disminuir el stock mediante el método `vender()`.

### Usuario

La clase `Usuario` representa a las personas registradas en el sistema.

Contiene:

* Identificación
* Nombre
* Correo

También realiza validaciones básicas de los datos y permite convertir la información a un diccionario para su almacenamiento en JSON.

### Venta

La clase `Venta` representa la relación entre un usuario y un producto vendido.

Contiene:

* Identificación del usuario
* Código del producto
* Cantidad vendida

La venta únicamente se registra cuando el usuario y el producto existen y existe suficiente stock.

### Restaurante

La clase `Restaurante` contiene la lógica principal del sistema.

Administra las colecciones de:

* Productos
* Usuarios
* Ventas

También se encarga de registrar productos y usuarios, buscar información, realizar ventas y consultar las ventas de un usuario.

### ArchivoServicio

`ArchivoServicio` se encarga de la persistencia de información mediante archivos JSON.

Administra:

* `productos.json`
* `usuarios.json`
* `ventas.json`

Utiliza `json.dump()` para guardar información y `json.load()` para recuperarla.

### main.py

Es el punto de entrada de la aplicación.

Presenta el menú al usuario, solicita información mediante `input()` y ejecuta las operaciones utilizando los métodos de `Restaurante`.

## Funcionamiento del stock

Cada producto posee una cantidad disponible mediante el atributo `stock`.

Antes de realizar una venta se verifica:

1. Que el usuario exista.
2. Que el producto exista.
3. Que la cantidad sea mayor que cero.
4. Que exista stock suficiente.

Cuando la venta es válida, se registra la venta y se descuenta la cantidad correspondiente del stock.

Por ejemplo:

```text
Stock inicial: 10
Cantidad vendida: 2
Stock restante: 8
```

No se permite que el stock llegue a un valor negativo.

## Relación Usuario - Producto mediante Venta

La operación principal de esta semana relaciona un usuario con un producto mediante una instancia de `Venta`.

El proceso es:

```text
Usuario
   ↓
Producto
   ↓
Validación de datos
   ↓
Venta
   ↓
Registro en colección de ventas
   ↓
Disminución del stock
```

La colección de ventas almacena objetos `Venta`, manteniendo la relación entre los usuarios y los productos vendidos.

## Persistencia JSON

El sistema utiliza tres archivos JSON:

### productos.json

Almacena los productos registrados y su stock actualizado.

### usuarios.json

Almacena los usuarios registrados.

### ventas.json

Almacena las ventas realizadas, incluyendo la identificación del usuario, el código del producto y la cantidad vendida.

Al iniciar el programa, los archivos JSON son leídos y sus datos son reconstruidos nuevamente como objetos de las clases correspondientes.

## Manejo de excepciones

El sistema controla diferentes situaciones mediante excepciones específicas:

* `FileNotFoundError`: permite iniciar con una colección vacía cuando un archivo todavía no existe.
* `json.JSONDecodeError`: controla archivos que contienen información JSON inválida.
* `PermissionError`: controla problemas de permisos de lectura o escritura.
* `KeyError`: controla registros JSON que no contienen las claves esperadas.
* `ValueError`: controla errores en las validaciones de productos, usuarios y ventas.

## Operaciones disponibles

El menú principal permite:

1. Registrar producto.
2. Listar productos.
3. Registrar usuario.
4. Listar usuarios.
5. Vender producto.
6. Consultar ventas de un usuario.
7. Salir.

## Pruebas realizadas

Se realizaron pruebas para comprobar el funcionamiento de la aplicación.

### Prueba de venta

Se registró un usuario y un producto con stock disponible.

```text
Producto: Hamburguesa
Stock inicial: 10
Cantidad vendida: 2
Stock restante: 8
```

La venta fue registrada correctamente y el stock fue actualizado.

### Consulta de ventas

Se consultaron las ventas utilizando la identificación del usuario y se obtuvo la venta registrada junto con el producto y la cantidad adquirida.

### Persistencia

Se verificó que los datos sean almacenados en:

```text
productos.json
usuarios.json
ventas.json
```

Los archivos permiten conservar la información para recuperarla posteriormente al ejecutar nuevamente el programa.

### Validación de stock

También se contempla el rechazo de una venta cuando la cantidad solicitada es mayor que el stock disponible, evitando que el stock quede en valores negativos.

## Ejecución

Para ejecutar el programa se debe ingresar a la carpeta `restaurante_app` y ejecutar:

```bash
python main.py
```

También puede utilizarse el intérprete de Python instalado en el equipo.

## Conclusión

La Semana 11 permitió ampliar el proyecto `restaurante_app` mediante el uso de colecciones de objetos para representar productos, usuarios y ventas. Se incorporó la relación entre usuarios y productos mediante la clase `Venta`, junto con el control de stock y la persistencia de información mediante archivos JSON.

El sistema mantiene una organización modular, separando los modelos, la lógica de negocio, la persistencia y la interacción con el usuario.
