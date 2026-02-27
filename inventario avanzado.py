import os


# --- 1. CLASE PRODUCTO ---
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        # Atributos requeridos: ID único, nombre, cantidad y precio
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Métodos para obtener (getters) y establecer (setters)
    def get_id(self): return self.id_producto

    def get_nombre(self): return self.nombre

    def get_cantidad(self): return self.cantidad

    def get_precio(self): return self.precio

    def set_cantidad(self, cantidad): self.cantidad = cantidad

    def set_precio(self, precio): self.precio = precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Stock: {self.cantidad} | Precio: ${self.precio:.2f}"


# --- 2. CLASE INVENTARIO ---
class Inventario:
    def __init__(self, archivo="inventario_datos.txt"):
        self.archivo = archivo
        # REQUISITO: Utilizar una colección adecuada (DICCIONARIO)
        self.productos = {}
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        """Serialización: Guarda la colección en el archivo"""
        try:
            with open(self.archivo, "w") as f:
                for p in self.productos.values():
                    # Formato simple para el TXT
                    f.write(f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
        except PermissionError:
            print("Error: No se tienen permisos para escribir en el archivo.")

    def cargar_desde_archivo(self):
        """Deserialización: Carga el archivo al iniciar el programa"""
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, "r") as f:
                    for linea in f:
                        id_p, nom, cant, prec = linea.strip().split(",")
                        # Creamos el objeto y lo metemos al diccionario usando el ID como llave
                        self.productos[id_p] = Producto(id_p, nom, int(cant), float(prec))
            except Exception:
                print("Aviso: No se pudo cargar el inventario previo o el archivo está vacío.")

    def añadir_producto(self, producto):
        """Añadir nuevos productos"""
        if producto.get_id() in self.productos:
            print("Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar_en_archivo()
            print("¡Producto añadido con éxito!")

    def eliminar_producto(self, id_producto):
        """Eliminar productos por ID"""
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado correctamente.")
        else:
            print("Error: No se encontró el ID.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """Actualizar cantidad o precio de un producto"""
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            self.guardar_en_archivo()
            print("Producto actualizado.")
        else:
            print("Error: ID no encontrado.")

    def buscar_por_nombre(self, nombre):
        """Buscar productos por nombre"""
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        if encontrados:
            print(f"\nResultados para '{nombre}':")
            for p in encontrados:
                print(p)
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_inventario(self):
        """Mostrar todos los productos en el inventario"""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            print("\n--- INVENTARIO ACTUAL ---")
            for p in self.productos.values():
                print(p)


# --- 3. INTERFAZ DE USUARIO ---
def ejecutar_menu():
    mi_inventario = Inventario()

    while True:
        print("\n--- GESTIÓN AVANZADA DE INVENTARIO ---")
        print("1. Añadir Producto")
        print("2. Eliminar por ID")
        print("3. Actualizar Cantidad/Precio")
        print("4. Buscar por Nombre")
        print("5. Mostrar Todo")
        print("6. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            id_p = input("ID único: ")
            nom = input("Nombre: ")
            cant = int(input("Cantidad: "))
            prec = float(input("Precio: "))
            mi_inventario.añadir_producto(Producto(id_p, nom, cant, prec))

        elif opcion == "2":
            id_p = input("Ingrese el ID a eliminar: ")
            mi_inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID del producto a actualizar: ")
            c_input = input("Nueva cantidad (deje en blanco para no cambiar): ")
            p_input = input("Nuevo precio (deje en blanco para no cambiar): ")

            cant = int(c_input) if c_input else None
            prec = float(p_input) if p_input else None
            mi_inventario.actualizar_producto(id_p, cant, prec)

        elif opcion == "4":
            nombre = input("Nombre del producto a buscar: ")
            mi_inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            mi_inventario.mostrar_inventario()

        elif opcion == "6":
            print("Cerrando sistema avanzado. ¡Éxito en tu tarea!")
            break


if __name__ == "__main__":
    ejecutar_menu()