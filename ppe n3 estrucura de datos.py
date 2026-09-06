import time


class BibliotecaManager:
    """
    Clase que gestiona el registro de libros de una biblioteca utilizando
    diccionarios (mapas) y conjuntos (sets) para optimizar el rendimiento.
    """

    def __init__(self):
        # Diccionario: Clave = ISBN (String), Valor = Datos del libro (Dict)
        self.libros = {}

        # Conjuntos: Almacenan elementos únicos sin importar el orden
        self.categorias = set()
        self.autores = set()

    def registrar_libro(self, isbn, titulo, autor, categoria, anio):
        """
        Registra un libro nuevo. Si el ISBN ya existe, levanta una advertencia.
        """
        if isbn in self.libros:
            print(f"[ALERTA] El libro con ISBN {isbn} ya está registrado.")
            return False

        # Inserción en el Diccionario (Mapa) - Complejidad O(1)
        self.libros[isbn] = {
            "titulo": titulo,
            "autor": autor,
            "categoria": categoria,
            "anio": anio
        }

        # Inserción en Conjuntos (Sets) - Evitan duplicados automáticamente - Complejidad O(1)
        self.autores.add(autor)
        self.categorias.add(categoria)

        print(f"[ÉXITO] Libro '{titulo}' registrado correctamente.")
        return True

    def buscar_libro_por_isbn(self, isbn):
        """
        Búsqueda directa usando la clave del diccionario.
        Retorna el tiempo de ejecución y los datos.
        """
        inicio_tiempo = time.perf_counter()

        # Búsqueda en diccionario
        libro = self.libros.get(isbn, None)

        fin_tiempo = time.perf_counter()
        tiempo_ejecucion = fin_tiempo - inicio_tiempo

        return libro, tiempo_ejecucion

    def reporteria_inventario(self):
        """
        Visualiza los elementos de las estructuras de datos (Reportería).
        """
        print("\n" + "=" * 50)
        print("REPORTERÍA DEL SISTEMA DE BIBLIOTECA")
        print("=" * 50)

        # Mostrar Diccionario
        print(f"Total de libros registrados: {len(self.libros)}")
        for isbn, datos in self.libros.items():
            print(f" - ISBN: {isbn} | {datos['titulo']} ({datos['anio']}) - {datos['autor']}")

        # Mostrar Conjuntos
        print("\n[+] Categorías Disponibles (Sin duplicados):")
        for cat in sorted(self.categorias):
            print(f"  * {cat}")

        print("\n[+] Autores Registrados (Sin duplicados):")
        for autor in sorted(self.autores):
            print(f"  * {autor}")
        print("=" * 50 + "\n")


# ==========================================
# ESCENARIO DE PRUEBA Y EJECUCIÓN (MAIN)
# ==========================================
if __name__ == "__main__":
    sistema = BibliotecaManager()

    # 1. Carga de Datos (Demostrando el control de duplicados en sets)
    sistema.registrar_libro("978-3-16-148410-0", "Estructura de Datos", "Mark Allen Weiss", "Computación", 2021)
    sistema.registrar_libro("978-0-262-03384-8", "Introducción a los Algoritmos", "Thomas H. Cormen", "Algoritmia",
                            2022)
    sistema.registrar_libro("978-1-118-29027-9", "Fundamentos de Python", "Mark Allen Weiss", "Computación", 2020)
    sistema.registrar_libro("978-3-16-148410-0", "Estructura de Datos", "Mark Allen Weiss", "Computación",
                            2021)  # Intento duplicado

    # 2. Generación de Reportería
    sistema.reporteria_inventario()

    # 3. Prueba de Búsqueda y Tiempo de Ejecución (Para la sección de Análisis)
    isbn_buscado = "978-0-262-03384-8"
    resultado, tiempo = sistema.buscar_libro_por_isbn(isbn_buscado)

    if resultado:
        print(f"Búsqueda exitosa del ISBN {isbn_buscado}: '{resultado['titulo']}'")
        # Mostramos el tiempo en notación científica o decimales altos debido a la rapidez de O(1)
        print(f"Tiempo de ejecución de la búsqueda: {tiempo:.8f} segundos")

