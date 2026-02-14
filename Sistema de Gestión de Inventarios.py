# --- CLASE PRODUCTO ---
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters
    def get_id(self): return self.id_producto

    def get_nombre(self): return self.nombre

    def get_cantidad(self): return self.cantidad

    def get_precio(self): return self.precio

    # Setters
    def set_cantidad(self, cantidad): self.cantidad = cantidad

    def set_precio(self, precio): self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"


# --- CLASE INVENTARIO ---
class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: Ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None: p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None: p.set_precio(nuevo_precio)
                print("Producto actualizado.")
                return
        print("Error: Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        return resultados

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        for p in self.productos:
            print(p)


# --- INTERFAZ DE USUARIO (MENÚ) ---
def menu():
    mi_inventario = Inventario()

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar por Nombre")
        print("5. Mostrar Todo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_p = input("ID único: ")
            nom = input("Nombre: ")
            cant = int(input("Cantidad: "))
            prec = float(input("Precio: "))
            mi_inventario.añadir_producto(Producto(id_p, nom, cant, prec))

        elif opcion == "2":
            id_p = input("ID del producto a eliminar: ")
            mi_inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ")
            cant_input = input("Nueva cantidad (vacío para omitir): ")
            prec_input = input("Nuevo precio (vacío para omitir): ")

            cant = int(cant_input) if cant_input else None
            prec = float(prec_input) if prec_input else None
            mi_inventario.actualizar_producto(id_p, cant, prec)

        elif opcion == "4":
            nom = input("Nombre a buscar: ")
            resultados = mi_inventario.buscar_por_nombre(nom)
            if resultados:
                for r in resultados: print(r)
            else:
                print("No se encontraron coincidencias.")

        elif opcion == "5":
            mi_inventario.mostrar_todos()

        elif opcion == "6":
            print("Cerrando sistema...")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    menu()