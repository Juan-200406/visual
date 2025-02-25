import json

class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id_producto

    def establecer_id(self, id_producto):
        self.id_producto = id_producto

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_cantidad(self):
        return self.cantidad

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}  # Usamos un diccionario para un acceso rápido por ID

    def agregar_producto(self, producto):
        self.productos[producto.obtener_id()] = producto

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            if cantidad is not None:
                producto.establecer_cantidad(cantidad)
            if precio is not None:
                producto.establecer_precio(precio)
        else:
            print("Producto no encontrado.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [producto for producto in self.productos.values() if nombre.lower() in producto.obtener_nombre().lower()]
        return resultados

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, nombre_archivo="inventario.json"):
        datos_serializados = {id_producto: producto.__dict__ for id_producto, producto in self.productos.items()}
        with open(nombre_archivo, 'w') as archivo:
            json.dump(datos_serializados, archivo, indent=4)

    def cargar_inventario(self, nombre_archivo="inventario.json"):
        try:
            with open(nombre_archivo, 'r') as archivo:
                datos_serializados = json.load(archivo)
                for id_producto, datos_producto in datos_serializados.items():
                    producto = Producto(datos_producto['id_producto'], datos_producto['nombre'], datos_producto['cantidad'], datos_producto['precio'])
                    self.productos[id_producto] = producto
        except FileNotFoundError:
            print("Archivo de inventario no encontrado. Se creará uno nuevo.")

def menu(inventario):
    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar inventario")
        print("6. Guardar inventario")
        print("7. Cargar inventario")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_producto = int(input("ID del producto: "))
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)
        elif opcion == '2':
            id_producto = int(input("ID del producto a eliminar: "))
            inventario.eliminar_producto(id_producto)
        elif opcion == '3':
            id_producto = int(input("ID del producto a actualizar: "))
            cantidad = input("Nueva cantidad (dejar en blanco para no cambiar): ")
            precio = input("Nuevo precio (dejar en blanco para no cambiar): ")
            inventario.actualizar_producto(id_producto, int(cantidad) if cantidad else None, float(precio) if precio else None)
        elif opcion == '4':
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_producto_por_nombre(nombre)
            for producto in resultados:
                print(producto)
        elif opcion == '5':
            inventario.mostrar_inventario()
        elif opcion == '6':
            inventario.guardar_inventario()
        elif opcion == '7':
            inventario.cargar_inventario()
        elif opcion == '8':
            break
        else:
            print("Opción no válida.")

# Ejemplo de uso
inventario = Inventario()
inventario.cargar_inventario() #Carga el inventario al iniciar el programa.
menu(inventario)
inventario.guardar_inventario() #Guarda el inventario al salir del programa.