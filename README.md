# SimuladorTienda

**Descripción:**

El Proyecto de Simulador de Tienda es una aplicación de consola que simula una tienda en línea donde los usuarios pueden navegar por diferentes productos, agregar productos al carrito de compras y realizar pedidos. Los usuarios podrán ver detalles de los productos, como su nombre, descripción, precio y categoria, así como realizar búsquedas, añadir, eliminar y editar productos del carrito y filtrar productos.

**Funcionamiento:**

El proyecto está dividido en dos archivos principales:

1. `modelos.py`: Este archivo contiene las clases que representan los modelos de datos del proyecto, como `Carrito`, `Producto` y `Tienda`. Además, incluye clases para implementar estrategias de actualización de cantidad y descuento.

2. `SimuladorTienda.py`: Este archivo contiene la lógica principal del simulador de tienda. Aquí se encuentra la interacción con el usuario, la visualización de productos, la gestión del carrito de compras, la aplicación de descuentos y la realización de pedidos.

**Patrones de diseño utilizados:**

1. **Patrón Singleton (Singleton Pattern):** Se implementa en la clase `Tienda`. Este patrón asegura que solo exista una instancia de la clase `Tienda` en toda la aplicación. Esto garantiza que los datos de la tienda sean consistentes y compartidos entre todas las partes del programa.

2. **Patrón Strategy (Strategy Pattern):** Se implementa en las clases `ActualizacionCantidadStrategy` y `DescuentoStrategy`. Este patrón permite definir una familia de algoritmos intercambiables y encapsular cada uno de ellos, lo que facilita la modificación o extensión del comportamiento sin afectar a otras partes del código. Por ejemplo, la estrategia de descuento puede ser cambiada dinámicamente sin modificar el código que la utiliza.

**¿Cómo funciona cada parte del código?**

- **modelos.py:**
  - `Carrito`: Representa el carrito de compras y contiene métodos para agregar productos, aplicar descuentos y actualizar la estrategia de descuento.
  - `Producto`: Representa un producto en la tienda, con atributos como código, nombre, descripción, precio y categoría.
  - `Tienda`: Representa la tienda en línea y gestiona la lista de productos disponibles. Implementa el patrón Singleton para garantizar una única instancia de tienda en toda la aplicación.
  - `ActualizacionCantidadStrategy`: Define una interfaz para actualizar la cantidad de un producto en el carrito y proporciona implementaciones concretas para actualizar por nombre y por código.
  - `DescuentoStrategy`: Define una interfaz para aplicar descuentos y proporciona implementaciones concretas para distintos tipos de descuentos, como sin descuento y descuento del 10%.

- **SimuladorTienda.py:**
  - Contiene la lógica principal del simulador de tienda, incluyendo la interacción con el usuario, la visualización de productos, la gestión del carrito de compras, la aplicación de descuentos y la realización de pedidos.
  - Proporciona un menú de opciones para que el usuario interactúe con la tienda, como ver productos, ordenar productos, buscar productos por nombre, ver el carrito de compras, actualizar la cantidad de productos, aplicar descuentos y realizar pedidos.

**¿Por qué se implementaron los patrones de diseño?**

- **Patrón Singleton:** Se implementa para garantizar que solo exista una instancia de la tienda en toda la aplicación, lo que ayuda a mantener la consistencia de los datos y a evitar inconsistencias en la información de productos y carritos de compras.

- **Patrón Strategy:** Se implementa para permitir la fácil extensibilidad y modificación del comportamiento de actualización de cantidad y descuentos. Esto facilita la incorporación de nuevas estrategias de descuento o métodos de actualización de cantidad sin necesidad de modificar el código existente.

## Requerimientos

```bash
pip install colorama
```
```bash
pip install rich
```
**Autor:**

Este proyecto fue desarrollado por Tatiana Gutierrez R. 

**Fecha:**

28/03/2024
