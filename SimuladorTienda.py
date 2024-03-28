from colorama import init, Fore, Back, Style
from modelos import Carrito, Producto, Tienda, ActualizacionCantidadPorNombre, ActualizacionCantidadPorCodigo, Descuento10Porciento, SinDescuento
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

def mostrar_productos(tienda):
    print(Fore.MAGENTA + "╔═════════════════════════════════════════════════════════════════════════╗")
    print(Fore.MAGENTA + "║".ljust(26) + Fore.WHITE + "Productos Disponibles".ljust(48) + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "╠════════╦════════════════╦═════════╦═════════════════════════╦═══════════╣")
    print(Fore.MAGENTA + "║ " + Fore.WHITE + "Código" + Fore.MAGENTA + " ║ " + Fore.WHITE + "Nombre".ljust(15) + Fore.MAGENTA + "║ " +
          Fore.WHITE + "Precio".ljust(6) + Fore.MAGENTA + "  ║ " + Fore.WHITE + "Descripción".ljust(24) + Fore.MAGENTA + "║ " +
          Fore.WHITE + "Categoría" + Fore.MAGENTA + " ║")
    for producto in tienda.productos:
        print(Fore.MAGENTA + "╠════════╬════════════════╬═════════╬═════════════════════════╬═══════════╣")
        print(Fore.MAGENTA + "║ " + Fore.WHITE + str(producto.codigo).ljust(7) + Fore.MAGENTA + "║ " + Fore.WHITE +
              producto.nombre.ljust(15) + Fore.MAGENTA + "║ $" + Fore.WHITE + str(producto.precio).ljust(7) +
              Fore.MAGENTA + "║ " + Fore.WHITE + producto.descripcion.ljust(24) + Fore.MAGENTA + "║ " +
              Fore.WHITE + producto.categoria.ljust(10) + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "╚════════╩════════════════╩═════════╩═════════════════════════╩═══════════╝")

def mostrar_carrito(carrito, tienda):
    if not carrito.items:
        print(Fore.RED + "Por ahora no hay productos agregados al carrito.")
        return
    
    print(Fore.MAGENTA + "╔═══════════════════════════════════════════════════╗")
    print(Fore.MAGENTA + "║ " + Fore.WHITE + "Carrito de Compras".center(49) + Fore.MAGENTA + " ║")
    print(Fore.MAGENTA + "╠════════════╦══════════╦════════════╦══════════════╣")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " Nombre".ljust(12) + Fore.MAGENTA + "║" + Fore.WHITE + " Cantidad".ljust(10) +
          Fore.MAGENTA + "║" + Fore.WHITE + " Precio".ljust(12) + Fore.MAGENTA + "║" + Fore.WHITE + " Total".ljust(14) +
          Fore.MAGENTA + "║")

    #Diccionario temporal para almacenar las cantidades y precios de cada producto
    temp_dict = {}

    total_pedido = 0

    #Iterar sobre los productos en el carrito y mostrarlos con el precio actualizado
    for producto, cantidad, _ in carrito.items:
        if producto.nombre in temp_dict:
            temp_dict[producto.nombre][0] += cantidad
            temp_dict[producto.nombre][1] += producto.precio * cantidad
        else:
            temp_dict[producto.nombre] = [cantidad, producto.precio * cantidad]

    #Iterar sobre el diccionario de productos agrupados
    for nombre, (cantidad_total, total_precio) in temp_dict.items():
        if cantidad_total > 0:
            precio_unitario = total_precio / cantidad_total
        else:
            precio_unitario = 0
        total_producto_con_descuento = carrito.estrategia_descuento.calcular_precio_con_descuento(precio_unitario)
        total_producto = total_producto_con_descuento*cantidad_total

        print(Fore.MAGENTA + "╠════════════╬══════════╬════════════╬══════════════╣")
        print(Fore.MAGENTA + "║ " + Fore.WHITE + nombre.ljust(11) + Fore.MAGENTA + "║ " + Fore.WHITE +
              str(cantidad_total).ljust(9) + Fore.MAGENTA + "║ $" + Fore.WHITE + str(total_producto_con_descuento).ljust(10) +
              Fore.MAGENTA + "║ $" + Fore.WHITE + str(total_producto).ljust(12) + Fore.MAGENTA + "║")
        
        total_pedido += total_producto
    print(Fore.MAGENTA + "╠════════════╩══════════╩════════════╬══════════════╣")
    print(Fore.MAGENTA+"║ "+Fore.WHITE + "Total del carrito".ljust(35)+Fore.MAGENTA+"║"+Fore.MAGENTA+" $"
          +Fore.WHITE+str(total_pedido).ljust(12)+Fore.MAGENTA+"║")
    print(Fore.MAGENTA + "╚════════════════════════════════════╩══════════════╝")

    
def imprimir_pedido(nombre, celular, direccion, carrito):
    print("Su pedido es:")
    print(Fore.MAGENTA + "╔═══════════════════════════════════════════════════╗")
    linea = "╔═══════════════════════════════════════════════════╗"
    longitud_total = len(linea)
    contenido = f"{nombre} - {celular} - {direccion}"
    longitud_contenido = len(contenido)
    espacios_total = longitud_total - 2
    espacios_libres = espacios_total - longitud_contenido
    espacios_izquierda = espacios_libres // 2
    espacios_derecha = espacios_libres - espacios_izquierda
    print(Fore.MAGENTA + "║" + " " * espacios_izquierda + Fore.WHITE + contenido + " " * espacios_derecha + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "╠═════════════╦═══════════╦═══════════════╦═════════╣")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " Nombre".ljust(13) + Fore.MAGENTA + "║" + Fore.WHITE + " Cantidad".ljust(11) +
          Fore.MAGENTA + "║" + Fore.WHITE + "Precio unitario".ljust(15) + Fore.MAGENTA + "║" + Fore.WHITE + " Total".ljust(9) +
          Fore.MAGENTA + "║")

    #Diccionario temporal para almacenar las cantidades y precios de cada producto
    temp_dict = {}

    total_pedido = 0

    #Iterar sobre los productos en el carrito y mostrarlos con el precio actualizado
    for producto, cantidad, _ in carrito.items:
        if producto.nombre in temp_dict:
            temp_dict[producto.nombre][0] += cantidad
            temp_dict[producto.nombre][1] += producto.precio * cantidad
        else:
            temp_dict[producto.nombre] = [cantidad, producto.precio * cantidad]

    #Iterar sobre el diccionario de productos agrupados
    for nombre, (cantidad_total, total_precio) in temp_dict.items():
        precio_unitario = total_precio / cantidad_total
        total_producto_con_descuento = carrito.estrategia_descuento.calcular_precio_con_descuento(precio_unitario)
        total_producto = total_producto_con_descuento * cantidad_total

        print(Fore.MAGENTA + "╠═════════════╬═══════════╬═══════════════╬═════════╣")
        print(Fore.MAGENTA + "║ " + Fore.WHITE + nombre.ljust(12) + Fore.MAGENTA + "║ " + Fore.WHITE +
              str(cantidad_total).ljust(10) + Fore.MAGENTA + "║ $" + Fore.WHITE + str(total_producto_con_descuento).ljust(13) +
              Fore.MAGENTA + "║ $" + Fore.WHITE + str(total_producto).ljust(7) + Fore.MAGENTA + "║")

        total_pedido += total_producto
    print(Fore.MAGENTA + "╠═════════════╩═══════════╩════════════╦══╩═════════╣")
    print(Fore.MAGENTA + "║ " + Fore.WHITE + "Total del pedido".ljust(37) + Fore.MAGENTA + "║ $" + Fore.WHITE +
          str(total_pedido).ljust(10) + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "╚══════════════════════════════════════╩════════════╝")
    
def actualizar_cantidad_producto(carrito, tienda):
    nombre_producto = input("Ingrese el nombre del producto que desea actualizar: ")
    nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
    productos_en_carrito = [item[0] for item in carrito.items]
    if nombre_producto in [producto.nombre for producto in productos_en_carrito]:
        for i, (producto, cantidad, _) in enumerate(carrito.items):
            if producto.nombre.lower() == nombre_producto.lower():
                if nueva_cantidad == 0:
                    del carrito.items[i]  
                    #Eliminar el producto del carrito si la nueva cantidad es cero
                    print("Producto eliminado del carrito.")
                else:
                    carrito.items[i] = (producto, nueva_cantidad, producto.precio * nueva_cantidad)  # Actualizar cantidad
                    print("Cantidad actualizada.")
                return
    else:
        print("Producto no encontrado en el carrito.")

def buscar_productos_por_nombre(tienda):
    nombre_producto = input("Ingrese el nombre del producto que desea buscar: ")
    resultados = tienda.buscar_productos_por_nombre(nombre_producto)
    if resultados:
        print(Fore.MAGENTA + "╔════════════════════════════════════════════════════════════════╗")
        print(Fore.MAGENTA+"║                     " + Fore.WHITE + "Resultados de la Búsqueda" + Fore.MAGENTA + "                  ║")
        print(Fore.MAGENTA+"╠════════╦════════════════╦═══════════╦══════════════════════════╣")
        print(Fore.MAGENTA + "║ " + Fore.WHITE + "Código".ljust(6) +Fore.MAGENTA+ " ║ " + Fore.WHITE + "Nombre".ljust(15) +Fore.MAGENTA+ "║ " +
              Fore.WHITE + "Precio".ljust(10) +Fore.MAGENTA+ "║ " + Fore.WHITE + "Descripción" + Fore.MAGENTA + "              ║")
        for producto in resultados:
            print(Fore.MAGENTA + "╠════════╬════════════════╬═══════════╬══════════════════════════╣")
            print(Fore.MAGENTA + "║ " + Fore.WHITE + str(producto.codigo).ljust(7) +Fore.MAGENTA+ "║ " + Fore.WHITE + producto.nombre.ljust(15) +
                  Fore.MAGENTA+"║ $" +Fore.WHITE+ str(producto.precio).ljust(9) + Fore.MAGENTA+"║ "+Fore.WHITE+ producto.descripcion.ljust(25) + Fore.MAGENTA + "║")
        print(Fore.MAGENTA + "╚════════╩════════════════╩═══════════╩══════════════════════════╝")

def eliminar_producto_carrito(carrito):
    nombre_producto = input("Ingrese el nombre del producto que desea eliminar del carrito: ")
    for i, (producto, _, _) in enumerate(carrito.items):
        if producto.nombre.lower() == nombre_producto.lower():
            del carrito.items[i]  #Eliminar el producto del carrito
            print("Producto eliminado del carrito.")
            return
    print("Producto no encontrado en el carrito.")

def mostrar_menu():
    print(Fore.MAGENTA + "╔════════════════════════════════════════╗")
    print(Fore.MAGENTA + "║            " + Fore.WHITE + "Menú Principal" + Fore.MAGENTA + "              ║")
    print(Fore.MAGENTA + "╠════════════════════════════════════════╣")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " 1. Ver productos" + Fore.MAGENTA + "                       ║")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " 2. Ordenar productos" + Fore.MAGENTA + "                   ║")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " 3. Buscar productos por nombre" + Fore.MAGENTA + "         ║")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " 4. Ver carrito de compras" + Fore.MAGENTA + "              ║")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " 5. Actualizar cantidad de producto" + Fore.MAGENTA + "     ║")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " 6. Eliminar producto del carrito" + Fore.MAGENTA + "       ║")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " 7. Aplicar descuento" + Fore.MAGENTA + "                   ║")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " 8. Realizar pedido" + Fore.MAGENTA + "                     ║")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " 9. Salir" + Fore.MAGENTA + "                               ║")
    print(Fore.MAGENTA + "╚════════════════════════════════════════╝")

def opcion_ordenar_menu():
    print(Fore.MAGENTA + "╔════════════════════════════════════════╗")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " 1. Ordenar por precio".ljust(40) + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " 2. Ordenar por nombre".ljust(40) + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " 3. Ordenar por código".ljust(40) + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "║" + Fore.WHITE + " 4. Ordenar por categoria".ljust(40) + Fore.MAGENTA + "║")
    print(Fore.MAGENTA + "╚════════════════════════════════════════╝")

def main():
    carrito = Carrito()

    tienda = Tienda()
    tienda.agregar_producto(Producto(1, "Camisa", "Camisa de algodón", 25, "Ropa"))
    tienda.agregar_producto(Producto(2, "Pantalón", "Pantalón de drill", 40, "Ropa"))
    tienda.agregar_producto(Producto(3, "Zapatos", "Zapatos de cuero", 60, "Calzado"))
    tienda.agregar_producto(Producto(4, "Aretes", "Aretes de plata", 10, "Accesorios"))
    tienda.agregar_producto(Producto(5, "Medias", "Medias de lana", 15, "Ropa"))
    tienda.agregar_producto(Producto(6, "Gafas", "Gafas de sol", 20, "Accesorios"))
    tienda.agregar_producto(Producto(7, "Chaqueta", "Chaqueta de poliester", 35, "Ropa"))


    while True:
        console = Console()
        mensaje_bienvenida = "Bienvenido a la tienda de ropa de Tatiana"
        texto_personalizado = Text(mensaje_bienvenida, style="bold magenta")
        panel = Panel(texto_personalizado, title="", style="white on magenta", width=30, padding=(1, 2))
        console.print(panel)
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_productos(tienda)
            codigo_producto = int(input("Ingrese el código del producto que desea agregar al carrito: "))
            productos = tienda.buscar_productos_por_codigo(codigo_producto)
            if productos:
                producto = productos[0]
                cantidad = int(input("Ingrese la cantidad: "))
                carrito.agregar_producto(producto, cantidad)
                print(Fore.GREEN + "Producto agregado al carrito")
            else:
                print(Fore.RED + "Producto no encontrado")

        elif opcion == "2":
            opcion_ordenar_menu()
            opcion_ordenar = input("Seleccione cómo desea ordenar los productos: ")
            if opcion_ordenar == "1":
                tienda.ordenar_productos_por_precio()
            elif opcion_ordenar == "2":
                tienda.ordenar_productos_por_nombre()
            elif opcion_ordenar == "3":
                tienda.ordenar_productos_por_codigo()
            elif opcion_ordenar == "4":
                tienda.ordenar_productos_por_categoria()
            else:
                print(Fore.YELLOW + "Opción inválida")

        elif opcion == "3":
            buscar_productos_por_nombre(tienda)

        elif opcion == "4":
            mostrar_carrito(carrito, tienda)

        elif opcion == "5":
            actualizar_cantidad_producto(carrito, tienda)

        elif opcion == "6":
            eliminar_producto_carrito(carrito)

        elif opcion == "7":
            carrito.aplicar_descuento()

        elif opcion == "8":
            if carrito.items:
                print("Por favor, ingrese los siguientes datos para completar su pedido:")
                nombre = input("Nombre: ")
                celular = input("Número de celular: ")
                if len(celular) != 10 or not celular.isdigit():
                    print("Número de celular inválido.")
                else:
                    direccion = input("Dirección de entrega: ")
                    tipo_pago = input("\nTipo de pago (Efectivo/Tarjeta): ").lower()
                    if tipo_pago == "efectivo":
                        print(Fore.GREEN + "\nPedido realizado exitosamente.\n")
                    elif tipo_pago == "tarjeta":
                        print("Por favor, ingrese los datos de su tarjeta:")
                        numero_tarjeta = input("Número de tarjeta (10 dígitos): ")
                        while len(numero_tarjeta) != 10 or not numero_tarjeta.isdigit():
                            print("El número de tarjeta debe tener 10 dígitos.")
                            numero_tarjeta = input("Número de tarjeta (10 dígitos): ")
                        contraseña_tarjeta = input("Contraseña de tarjeta (5 caracteres): ")
                        while len(contraseña_tarjeta) != 5 or not contraseña_tarjeta.isdigit():
                            print("La contraseña de tarjeta debe tener 5 caracteres.")
                            contraseña_tarjeta = input("Contraseña de tarjeta (5 caracteres): ")
                        print("Datos de tarjeta ingresados correctamente.\n")
                        print(Fore.GREEN + "\nPedido realizado exitosamente.\n")

                    else:
                        print(Fore.RED + "Tipo de pago inválido.")
                        continue

                    imprimir_pedido(nombre, celular, direccion, carrito)

                    break
            else:
                print(Fore.RED + "El carrito de compras está vacío")

        elif opcion == "9":
            print("Gracias por visitar la tienda. ¡Vuelve pronto!")
            break

        else:
            print(Fore.YELLOW + "Opción inválida")

if __name__ == "__main__":
    main()
