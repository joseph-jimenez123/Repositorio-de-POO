# PROGRAMACIÓN ORIENTADA A OBJETOS (POO)
# Título: Cálculo del Promedio Semanal del Clima con POO

# Definición de la Clase
class ClimaSemanal:
    """
    Clase que representa el registro diario del clima para una semana.
    Aplica encapsulamiento al gestionar las temperaturas internamente.
    """

    def __init__(self):
        # Atributo para almacenar las temperaturas (Encapsulamiento)
        self.__temperaturas = []
        self.__dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    # Método para ingresar los datos diarios
    def ingresar_temperaturas(self):
        """
        Solicita al usuario las temperaturas diarias y las almacena en el objeto.
        """
        print("--- Ingreso de Temperaturas Diarias (POO) ---")
        self.__temperaturas = []  # Asegura que esté vacía antes de ingresar
        for dia in self.__dias_semana:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del {dia}: "))
                    # Almacena el dato directamente en el atributo de la instancia
                    self.__temperaturas.append(temp)
                    break
                except ValueError:
                    print("Error: Por favor, ingrese un número válido.")

    # Método para calcular el promedio semanal
    def calcular_promedio_semanal(self):
        """
        Calcula el promedio de las temperaturas almacenadas en la instancia.
        Retorna: El promedio (flotante) o 0 si no hay datos.
        """
        if not self.__temperaturas:
            return 0

        suma = sum(self.__temperaturas)
        promedio = suma / len(self.__temperaturas)
        return promedio

    # Método "Getter" para acceder a las temperaturas (Buena práctica de POO)
    def obtener_temperaturas(self):
        """
        Proporciona acceso seguro a la lista de temperaturas registradas.
        """
        return self.__temperaturas


# Función principal para la ejecución con POO
def main_poo():
    """
    Función principal que utiliza la clase ClimaSemanal.
    """
    print("\n--- INICIO: Programa de Promedio Semanal (POO) ---")

    # 1. Crear una instancia (objeto) de la clase
    clima_semana = ClimaSemanal()

    # 2. Utilizar el método para ingresar los datos
    clima_semana.ingresar_temperaturas()

    # 3. Utilizar el método para calcular el resultado
    promedio = clima_semana.calcular_promedio_semanal()

    # 4. Mostrar el resultado
    print("\n--- Resultados ---")
    print(f"Temperaturas registradas: {clima_semana.obtener_temperaturas()}")
    print(f"El promedio semanal del clima es: {promedio:.2f}")
    print("--- FIN: Programa de Promedio Semanal (POO) ---\n")


# Ejecución del programa
if __name__ == "__main__":
    main_poo()