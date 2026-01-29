# Tarea: Aplicación de Conceptos de POO - Ejemplo Personajes de Juego

# 1. CLASE BASE: Define un personaje genérico
class Personaje:
    def __init__(self, nombre, nivel):
        self.nombre = nombre
        self.nivel = nivel
        # ENCAPSULACIÓN: Los puntos de vida son privados (__vida)
        # Nadie puede modificarlos directamente desde fuera
        self.__vida = 100

    def presentarse(self):
        print(f"Soy {self.nombre} y soy nivel {self.nivel}.")

    # Método para Polimorfismo
    def usar_habilidad(self):
        print("El personaje realiza una acción básica.")

    # Getter para la Encapsulación (permite leer la vida de forma segura)
    def ver_estado_salud(self):
        return f"Vida actual de {self.nombre}: {self.__vida} HP"

# 2. CLASE DERIVADA (Herencia): El Guerrero "es un" Personaje
class Guerrero(Personaje):
    def __init__(self, nombre, nivel, arma):
        # Heredamos los atributos del Personaje
        super().__init__(nombre, nivel)
        self.arma = arma

    # 3. POLIMORFISMO: El Guerrero usa su habilidad de forma distinta
    def usar_habilidad(self):
        print(f"¡{self.nombre} ataca ferozmente con su {self.arma}!")

# --- PRUEBA DEL PROGRAMA (Instancias) ---

# Creamos un personaje genérico
sujeto_extra = Personaje("Aldeano", 1)
sujeto_extra.presentarse()
sujeto_extra.usar_habilidad()

print("-" * 30)

# Creamos un Guerrero (Herencia)
mi_heroe = Guerrero("Ragnar", 10, "Hacha doble")
mi_heroe.presentarse()  # Usa el método de la clase padre
mi_heroe.usar_habilidad() # Usa su propio método (Polimorfismo)

# Intentamos ver la vida (Encapsulación)
print(mi_heroe.ver_estado_salud())