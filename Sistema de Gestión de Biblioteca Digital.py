# --- 1. CLASE LIBRO ---
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # REQUISITO: Usar una tupla para título y autor (datos inmutables)
        self.datos_inmutables = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"'{self.datos_inmutables[0]}' por {self.datos_inmutables[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# --- 2. CLASE USUARIO ---
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        # REQUISITO: Lista para libros actualmente prestados
        self.libros_prestados = []

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# --- 3. CLASE BIBLIOTECA ---
class Biblioteca:
    def __init__(self):
        # REQUISITO: Diccionario para libros disponibles (ISBN como clave)
        self.libros = {}
        # REQUISITO: Conjunto (Set) para IDs de usuario únicos
        self.usuarios_ids = set()
        self.usuarios = {}

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")
        else:
            print("Error: El ISBN ya existe.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios_ids:
            self.usuarios_ids.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("Error: El ID de usuario ya está en uso.")

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            libro = self.libros.pop(isbn)  # Lo quitamos de disponibles
            self.usuarios[id_usuario].libros_prestados.append(libro)
            print(f"Libro '{libro.datos_inmutables[0]}' prestado a {self.usuarios[id_usuario].nombre}.")
        else:
            print("Error: Usuario o Libro no encontrado.")

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for i, libro in enumerate(usuario.libros_prestados):
                if libro.isbn == isbn:
                    libro_devuelto = usuario.libros_prestados.pop(i)
                    self.libros[isbn] = libro_devuelto  # Vuelve a estar disponible
                    print(f"Libro '{libro_devuelto.datos_inmutables[0]}' devuelto.")
                    return
            print("Error: El usuario no tiene ese libro.")
        else:
            print("Error: Usuario no encontrado.")

    def buscar_libro(self, criterio):
        print(f"\nBuscando '{criterio}':")
        encontrados = [l for l in self.libros.values() if criterio.lower() in l.datos_inmutables[0].lower()
                       or criterio.lower() in l.datos_inmutables[1].lower()
                       or criterio.lower() in l.categoria.lower()]
        for l in encontrados: print(l)


# --- PRUEBA DEL SISTEMA ---
if __name__ == "__main__":
    mi_biblioteca = Biblioteca()

    # Crear libros y usuarios
    l1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Ficción", "101")
    u1 = Usuario("Joseph Jimenez", "U001")

    # Operaciones
    mi_biblioteca.añadir_libro(l1)
    mi_biblioteca.registrar_usuario(u1)
    mi_biblioteca.prestar_libro("U001", "101")
    mi_biblioteca.devolver_libro("U001", "101")
    mi_biblioteca.buscar_libro("Ficción")