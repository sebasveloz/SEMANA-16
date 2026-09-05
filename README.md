# restaurante_app - Semana 12

## Estudiante

**Anthony Sebastian Veloz Morales**

## Descripción

El proyecto `restaurante_app` corresponde a una aplicación desarrollada en Python utilizando Programación Orientada a Objetos y una arquitectura modular.

En esta Semana 12 se mantiene la funcionalidad desarrollada en la Semana 11 y se mejora el rendimiento de las búsquedas y consultas mediante el uso adecuado de colecciones.

El sistema permite registrar productos y usuarios, realizar ventas, controlar el stock disponible, consultar las ventas de un usuario y conservar la información mediante archivos JSON.

## Objetivo de la Semana 12

La mejora principal consiste en evitar recorridos completos e innecesarios de las listas cuando se conoce una clave de búsqueda.

Para ello se mantienen las listas principales y se incorporan diccionarios auxiliares que funcionan como índices en memoria.

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

## Colecciones utilizadas

El sistema conserva las listas principales:

```python
self._productos
self._usuarios
self._ventas
```

Estas colecciones continúan siendo utilizadas para almacenar, recorrer, listar y persistir los objetos.

Además, se incorporaron los siguientes índices auxiliares:

### Índice de productos

```python
self._indice_productos: dict[str, Producto]
```

La clave utilizada es el código del producto.

Permite realizar una búsqueda directamente:

```python
self._indice_productos.get(codigo)
```

De esta manera se evita recorrer toda la lista de productos cada vez que se necesita localizar un producto.

### Índice de usuarios

```python
self._indice_usuarios: dict[str, Usuario]
```

La clave utilizada es la identificación del usuario.

La búsqueda se realiza mediante:

```python
self._indice_usuarios.get(identificacion)
```

Esto permite localizar rápidamente un usuario por su identificación.

### Índice de ventas por usuario

```python
self._indice_ventas_usuario: dict[str, list[Venta]]
```

Este índice agrupa las ventas según la identificación del usuario.

Cuando se consulta las ventas de un usuario, se obtiene directamente la lista correspondiente:

```python
self._indice_ventas_usuario.get(
    identificacion_usuario,
    []
)
```

Así se evita recorrer toda la colección de ventas para cada consulta.

## Reconstrucción de índices

Al iniciar el programa se cargan los productos, usuarios y ventas desde los archivos JSON.

Después de recuperar los objetos se ejecuta:

```python
self._reconstruir_indices()
```

Este método reconstruye los tres índices en memoria a partir de las colecciones principales.

De esta forma, los diccionarios auxiliares no necesitan ser almacenados en los archivos JSON y pueden volver a generarse cada vez que se inicia el sistema.

## Sincronización de los índices

Los índices se mantienen sincronizados con las colecciones principales.

Cuando se registra un producto:

```python
self._productos.append(producto)
self._indice_productos[producto.codigo] = producto
```

Cuando se registra un usuario:

```python
self._usuarios.append(usuario)
self._indice_usuarios[usuario.identificacion] = usuario
```

Cuando se registra una venta:

```python
self._ventas.append(venta)
```

y la venta también se agrega al índice correspondiente:

```python
self._indice_ventas_usuario[
    usuario.identificacion
].append(venta)
```

De esta manera las listas principales y los índices representan la misma información.

## Uso de las colecciones

Las colecciones tienen responsabilidades diferentes.

### Listas

Las listas se utilizan como colecciones principales para:

* almacenar objetos;
* recorrer información;
* listar productos;
* listar usuarios;
* mantener todas las ventas;
* persistir los datos en JSON.

### Diccionarios

Los diccionarios se utilizan como índices auxiliares para:

* búsqueda de productos por código;
* búsqueda de usuarios por identificación;
* consulta de ventas por usuario.

No se reemplazaron las listas principales por diccionarios porque ambas estructuras cumplen responsabilidades diferentes.

## Ventas y control de stock

El sistema conserva la relación:

```text
Usuario
   ↓
Venta
   ↓
Producto
```

Antes de registrar una venta se verifica:

1. Que el usuario exista.
2. Que el producto exista.
3. Que la cantidad sea mayor que cero.
4. Que exista stock suficiente.

Cuando la venta es válida, se registra en la colección de ventas y se actualiza el stock del producto.

Ejemplo:

```text
Stock inicial: 10
Cantidad vendida: 2
Stock restante: 8
```

No se permite realizar una venta superior al stock disponible.

## Persistencia JSON

La información continúa almacenándose mediante tres archivos:

```text
datos/productos.json
datos/usuarios.json
datos/ventas.json
```

Los objetos se convierten a diccionarios antes de ser guardados y posteriormente se reconstruyen como objetos cuando el programa inicia.

Los índices auxiliares no se guardan en JSON porque son estructuras temporales en memoria. Se reconstruyen automáticamente a partir de las listas cargadas.

## Funcionalidades

El menú principal mantiene las funcionalidades desarrolladas previamente:

1. Registrar producto.
2. Listar productos.
3. Registrar usuario.
4. Listar usuarios.
5. Vender producto.
6. Consultar ventas de un usuario.
7. Salir.

## Mejoras realizadas

Las principales mejoras implementadas en esta semana son:

* búsqueda de productos mediante un diccionario indexado por código;
* búsqueda de usuarios mediante un diccionario indexado por identificación;
* consulta de ventas agrupadas por usuario;
* reconstrucción automática de índices al iniciar el programa;
* actualización de los índices al registrar información;
* conservación de las listas principales;
* mantenimiento de la persistencia JSON;
* conservación del control de stock;
* mantenimiento de la lógica de negocio dentro de `Restaurante`.

## Pruebas realizadas

Se realizaron las siguientes comprobaciones:

### 1. Búsqueda de producto

Se comprobó que un producto pueda ser localizado utilizando su código mediante el índice de productos.

### 2. Búsqueda de usuario

Se comprobó que un usuario pueda ser localizado utilizando su identificación mediante el índice de usuarios.

### 3. Consulta de ventas

Se comprobó que las ventas de un usuario puedan consultarse mediante el índice de ventas agrupadas por identificación.

### 4. Registro de venta

Se comprobó que una venta válida sea registrada correctamente y que el stock sea reducido.

### 5. Control de stock

Se verificó que el sistema no permita vender una cantidad superior al stock disponible.

### 6. Persistencia

Se verificó que productos, usuarios y ventas sean almacenados en los archivos JSON.

### 7. Reconstrucción de índices

Se cerró y volvió a ejecutar el programa para comprobar que los datos almacenados en JSON sean recuperados y que los índices auxiliares se reconstruyan correctamente.

## Ejecución

Para ejecutar el programa se debe ingresar a la carpeta `restaurante_app` y ejecutar:

```bash
python main.py
```

En caso de utilizar una instalación específica de Python también puede ejecutarse mediante el intérprete configurado en Visual Studio Code.

## Conclusión

La Semana 12 permitió mejorar el rendimiento interno de `restaurante_app` mediante el uso de colecciones auxiliares.

Se conservaron las listas principales para almacenar, recorrer y persistir los objetos, mientras que se incorporaron diccionarios como índices para realizar búsquedas frecuentes por código de producto e identificación de usuario.

También se implementó un índice para agrupar las ventas por usuario, reduciendo recorridos innecesarios al realizar consultas.

Los índices se mantienen sincronizados con las colecciones principales y se reconstruyen automáticamente después de recuperar los datos desde los archivos JSON.

De esta manera, el proyecto conserva las funcionalidades de la Semana 11 y mejora la eficiencia de sus búsquedas y consultas sin modificar innecesariamente la arquitectura del sistema.
