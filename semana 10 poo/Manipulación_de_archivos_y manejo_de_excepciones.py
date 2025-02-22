import os

class Inventario:
    def __init__(self, archivo_inventario="inventario.txt"):
        self.archivo_inventario = archivo_inventario
        self.inventario = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo_inventario, "r") as archivo:
                for linea in archivo:
                    try:
                        datos = linea.strip().split(",")
                        nombre = datos[0]
                        cantidad = int(datos[1])
                        self.inventario[nombre] = cantidad
                    except (ValueError, IndexError):
                        print(f"Error: Formato de línea incorrecto en {self.archivo_inventario}: {linea}")
        except FileNotFoundError:
            print(f"Advertencia: Archivo {self.archivo_inventario} no encontrado. Se creará uno nuevo.")
        except Exception as e:
            print(f"Error al cargar el inventario desde {self.archivo_inventario}: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo_inventario, "w") as archivo:
                for nombre, cantidad in self.inventario.items():
                    archivo.write(f"{nombre},{cantidad}\n")
            print(f"Inventario guardado exitosamente en {self.archivo_inventario}")
        except Exception as e:
            print(f"Error al guardar el inventario en {self.archivo_inventario}: {e}")

    def agregar_producto(self, nombre, cantidad):
        if nombre in self.inventario:
            self.inventario[nombre] += cantidad
        else:
            self.inventario[nombre] = cantidad
        self.guardar_inventario()

    def actualizar_producto(self, nombre, cantidad):
        if nombre in self.inventario:
            self.inventario[nombre] = cantidad
            self.guardar_inventario()
        else:
            print(f"Error: Producto '{nombre}' no encontrado en el inventario.")

    def eliminar_producto(self, nombre):
        if nombre in self.inventario:
            del self.inventario[nombre]
            self.guardar_inventario()
        else:
            print(f"Error: Producto '{nombre}' no encontrado en el inventario.")

    def mostrar_inventario(self):
        if self.inventario:
            print("Inventario:")
            for nombre, cantidad in self.inventario.items():
                print(f"- {nombre}: {cantidad}")
        else:
            print("El inventario está vacío.")

# Ejemplo de uso
inventario = Inventario()

inventario.agregar_producto("Camisa", 10)
inventario.agregar_producto("Pantalón", 5)
inventario.mostrar_inventario()

inventario.actualizar_producto("Camisa", 15)
inventario.mostrar_inventario()

inventario.eliminar_producto("Pantalón")
inventario.mostrar_inventario()