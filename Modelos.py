from colorama import Fore

class Carrito:
    #Clase para representar el carrito de compras del usuario
    #Permite agregar productos, aplicar descuentos y cambiar estrategias de descuento

    def __init__(self):
        self.items = []  #Lista de tuplas (producto, cantidad, total_producto_con_descuento)
        self.descuento_aplicado = False  #Indica si ya se aplicó el descuento
        self.descuento = 0.9  #Valor del descuento (10%)
        self.estrategia_descuento = SinDescuento()  #Estrategia de descuento por defecto

    def agregar_producto(self, producto, cantidad):
        total_producto_con_descuento = producto.precio * cantidad * self.descuento
        self.items.append((producto, cantidad, total_producto_con_descuento))

    def aplicar_descuento(self):
        self.estrategia_descuento.aplicar_descuento(self)

    def set_estrategia_descuento(self, estrategia):
        self.estrategia_descuento = estrategia

class Producto:
    def __init__(self, codigo, nombre, descripcion, precio, categoria):
        #Inicializar un producto con sus atributos
        self.codigo = codigo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria

class Tienda:
    #Clase para representar la tienda de productos

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.productos = []  #Lista de productos disponibles en la tienda
        return cls._instance

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def buscar_productos_por_nombre(self, nombre):
        resultados = []
        for producto in self.productos:
            if nombre.lower() in producto.nombre.lower():
                resultados.append(producto)
        return resultados

    def buscar_productos_por_codigo(self, codigo):
        resultados = []
        for producto in self.productos:
            if producto.codigo == codigo:
                resultados.append(producto)
        return resultados

    #Métodos para ordenar productos por precio, nombre, código o categoría
    def ordenar_productos_por_precio(self):
        self.productos.sort(key=lambda x: x.precio)

    def ordenar_productos_por_nombre(self):
        self.productos.sort(key=lambda x: x.nombre)

    def ordenar_productos_por_codigo(self):
        self.productos.sort(key=lambda x: x.codigo)
        
    def ordenar_productos_por_categoria(self):
        self.productos.sort(key=lambda x: x.categoria)

class ActualizacionCantidadStrategy:
    #Clase base para estrategias de actualización de cantidad de productos en el carrito

    def actualizar_cantidad(self, carrito, producto, nueva_cantidad):
        pass

class ActualizacionCantidadPorNombre(ActualizacionCantidadStrategy):
    #Estrategia de actualización de cantidad por nombre de producto

    def actualizar_cantidad(self, carrito, nombre_producto, nueva_cantidad):
        # Método para actualizar la cantidad de un producto por su nombre en el carrito
        for producto, cantidad, _ in carrito.items:
            if producto.nombre.lower() == nombre_producto.lower():
                carrito.items.remove((producto, cantidad, _))
                carrito.agregar_producto(producto, nueva_cantidad)
                print("Cantidad actualizada.")
                return
        print(Fore.RED + "Producto no encontrado en el carrito.")

class ActualizacionCantidadPorCodigo(ActualizacionCantidadStrategy):
    #Estrategia de actualización de cantidad por código de producto

    def actualizar_cantidad(self, carrito, codigo_producto, nueva_cantidad):
        #Método para actualizar la cantidad de un producto por su código en el carrito
        for producto, cantidad, _ in carrito.items:
            if producto.codigo == codigo_producto:
                carrito.items.remove((producto, cantidad, _))
                carrito.agregar_producto(producto, nueva_cantidad)
                print(Fore.GREEN + "Cantidad actualizada.")
                return
        print(Fore.RED + "Producto no encontrado en el carrito.")

class DescuentoStrategy:
    #Clase base para estrategias de descuento

    def aplicar_descuento(self, carrito):
        #Método abstracto para aplicar el descuento al carrito
        pass

    def calcular_precio_con_descuento(self, precio):
        #Método abstracto para calcular el precio con descuento
        pass

class SinDescuento(DescuentoStrategy):
    #Estrategia de descuento sin aplicar descuento

    def aplicar_descuento(self, carrito):
        #Método para aplicar la estrategia de descuento sin descuento
        if carrito.descuento_aplicado:
            print(Fore.YELLOW + "El descuento ya ha sido aplicado anteriormente.")
            return
        codigo_descuento = input("Ingrese el código de descuento (si no tiene, presione Enter): ")
        if codigo_descuento == "10OFF":
            carrito.estrategia_descuento = Descuento10Porciento()
            carrito.aplicar_descuento()
        else:
            print(Fore.RED + "Código de descuento inválido.")

    def calcular_precio_con_descuento(self, precio):
        return precio

class Descuento10Porciento(DescuentoStrategy):
    #Estrategia de descuento del 10%

    def aplicar_descuento(self, carrito):
        #Método para aplicar el descuento del 10% al carrito
        if carrito.descuento_aplicado:
            print(Fore.YELLOW + "El descuento ya ha sido aplicado anteriormente.")
            return carrito.descuento
        carrito.descuento_aplicado = True
        print(Fore.GREEN + "Descuento aplicado correctamente.")

        for i, (producto, cantidad, _) in enumerate(carrito.items):
            total_producto_con_descuento = producto.precio * cantidad * (1 - carrito.descuento)
            carrito.items[i] = (producto, cantidad, total_producto_con_descuento)

        return carrito.descuento

    def calcular_precio_con_descuento(self, precio):
        return precio * 0.9
