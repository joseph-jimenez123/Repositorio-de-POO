# Caso de Mundo Real: Sistema de Gestión de Préstamos de Biblioteca
# Este programa modela la interacción entre Libros y Miembros.

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        estado = "Disponible" if self.disponible else "Prestado"
        return f"'{self.titulo}' de {self.autor} [{estado}]"

class Miembro:
    def __init__(self, nombre, id_miembro):
        self.nombre = nombre
        self.id_miembro = id_miembro
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.disponible:
            libro.disponible = False
            self.libros_prestados.append(libro)
            print(f"Éxito: {self.nombre} ha retirado {libro.titulo}.")
        else:
            print(f"Error: {libro.titulo} ya está prestado.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            libro.disponible = True
            self.libros_prestados.remove(libro)
            print(f"Éxito: {self.nombre} ha devuelto {libro.titulo}.")

# Demostración
if __name__ == "__main__":
    libro1 = Libro("Cien años de soledad", "Gabo", "12345")
    usuario1 = Miembro("Joseph", "M001")
    
    usuario1.tomar_prestado(libro1)
    print(libro1)