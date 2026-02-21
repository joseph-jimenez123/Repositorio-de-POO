import os


# --- CLASE PRODUCTO ---
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    # Getters necesarios para guardar los datos correctamente
    def get_id(self): return self.id_producto

    def get_nombre(self): return self.nombre

    def get_cantidad(self): return self.cantidad

    def get_precio(self): return self.precio

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio}"


# --- CLASE INVENTARIO ---
class Inventario:
    def __init__(self, nombre_archivo="inventario.txt"):
        self.nombre_archivo = nombre_archivo
        self.productos = []
        # REQUISITO: Cargar automáticamente al iniciar
        self.cargar_desde_archivo()

    def guardar_en_archivo(self):
        """REQUISITO: Almacenamiento persistente en archivo TXT"""
        try:
            with open(self.nombre_archivo, "w") as archivo:
                for p in self.productos:
                    linea = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    archivo.write(linea)
        except PermissionError:
            # REQUISITO: Manejo de excepciones
            print("Error: No se tienen permisos para escribir en el archivo.")

    def cargar_desde_archivo(self):
        """REQUISITO: Recuperar datos del archivo"""
        if not os.path.exists(self.nombre_archivo):
            return

        try:
            with open(self.nombre_archivo, "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(",")
                    if len(datos) == 4:
                        p = Producto(datos[0], datos[1], int(datos[2]), float(datos[3]))
                        self.productos.append(p)
        except (FileNotFoundError, ValueError):
            # REQUISITO: Manejo de errores de formato o archivo
            print("Aviso: El archivo de inventario está vacío o tiene errores.")

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: El ID ya existe.")
                return
        self.productos.append(producto)
        self.guardar_en_archivo()  # Actualiza el archivo de inmediato
        print(f"Producto '{producto.get_nombre()}' guardado correctamente.")

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
        else:
            for p in self.productos:
                print(p)


# --- FUNCIÓN DEL MENÚ ---
def ejecutar_menu():
    mi_inventario = Inventario()

    while True:
        print("\n--- SISTEMA DE GESTIÓN (ARCHIVOS) ---")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Salir")

        opcion = input("Elija una opción: ")

        if opcion == "1":
            try:
                id_p = input("ID: ")
                nom = input("Nombre: ")
                cant = int(input("Cantidad (número): "))
                prec = float(input("Precio (número): "))
                mi_inventario.añadir_producto(Producto(id_p, nom, cant, prec))
            except ValueError:
                # REQUISITO: Manejo de errores en la interfaz
                print("Error: Ingrese números válidos para cantidad y precio.")
        elif opcion == "2":
            mi_inventario.mostrar_inventario()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break


# --- PUNTO DE ENTRADA (ESTO ES LO QUE HACÍA FALTA) ---
if __name__ == "__main__":
    ejecutar_menu()