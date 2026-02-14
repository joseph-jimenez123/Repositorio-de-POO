class Producto:
    def __init__(self, id_producto, nombre, valor):
        self.id_producto=id_producto
        self.nombre=nombre
        self.valor=valor

    class Inventario:
        def __init__(self):
            # Creamos una lista vacía para guardar los productos
            self.lista_productos = []

        def agregar(self, nuevo_producto):
            # .append() mete el objeto Producto dentro de la lista
            self.lista_productos.append(nuevo_producto)
            print(f"¡{nuevo_producto.get_nombre()} agregado con éxito!")

        def mostrar_todo(self):
            # Si la lista no tiene nada
            if not self.lista_productos:
                print("El inventario está vacío.")
            # Si tiene algo, recorremos la lista con un for
            for p in self.lista_productos:
                print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Valor: {p.get_valor()}")

    def get_id (self):
        return self.id_producto
    def get_nombre (self):
        return self.nombre
    def get_valor (self):
        return self.valor

    def set_valor (self, nuevo_valor):
        self.valor = nuevo_valor

class Inventario:
    def __init__(self):
        self.lista_productos = []

    # ASEGÚRATE DE QUE SE LLAME 'agregar' (todo en minúsculas)
    def agregar(self, nuevo_producto):
        self.lista_productos.append(nuevo_producto)
        print(f"¡{nuevo_producto.get_nombre()} agregado con éxito!")

    def mostrar_todo(self):
        if not self.lista_productos:
            print("El inventario está vacío.")
        else:
            for p in self.lista_productos:
                print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | Valor: {p.get_valor()}")

def ejecutar_menu():
    mi_bodega = Inventario()  # Creamos una instancia del inventario

    while True:  # Bucle infinito para que el programa no se cierre solo
        print("\n--- MI TIENDITA ---")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            # Pedimos los datos al usuario
            id_p = input("Escribe el ID: ")
            nom = input("Escribe el Nombre: ")
            val = input("Escribe el Valor: ")

            # Creamos el objeto Producto y lo pasamos a la función agregar
            nuevo = Producto(id_p, nom, val)
            mi_bodega.agregar(nuevo)

        elif opcion == "2":
            mi_bodega.mostrar_todo()

        elif opcion == "3":
            print("¡Adiós!")
            break  # Rompe el bucle while y cierra el programa
        else:
            print("Opción no válida.")


# Esto le dice a Python que empiece a correr el menú
if __name__ == "__main__":
    ejecutar_menu()
