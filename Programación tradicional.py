# PROGRAMACIÓN TRADICIONAL
# Título: Cálculo del Promedio Semanal del Clima

# 1. Función para la entrada de datos
def obtener_temperaturas_semanales():
    """
    Solicita al usuario las temperaturas diarias de una semana (7 días).
    Retorna: Una lista con 7 valores de temperatura (flotantes).
    """
    temperaturas = []
    dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    print("--- Ingreso de Temperaturas Diarias ---")
    for dia in dias_semana:
        while True:
            try:
                # Solicita la temperatura y la almacena en la lista
                temp = float(input(f"Ingrese la temperatura del {dia}: "))
                temperaturas.append(temp)
                break
            except ValueError:
                print("Error: Por favor, ingrese un número válido.")
    return temperaturas


# 2. Función para calcular el promedio
def calcular_promedio(datos):
    """
    Calcula el promedio de una lista de números.
    Recibe: Una lista de números (temperaturas).
    Retorna: El valor del promedio (flotante).
    """
    if not datos:
        return 0  # Manejo de lista vacía

    # Cálculo: Suma de todos los elementos dividida por la cantidad de elementos
    suma = sum(datos)
    promedio = suma / len(datos)
    return promedio


# 3. Función principal (Lógica de control)
def main_tradicional():
    """
    Función principal que coordina la ejecución de la lógica tradicional.
    """
    print("\n--- INICIO: Programa de Promedio Semanal (Tradicional) ---")

    # Paso 1: Obtener los datos
    datos_temperaturas = obtener_temperaturas_semanales()

    # Paso 2: Calcular el promedio
    promedio_semanal = calcular_promedio(datos_temperaturas)

    # Paso 3: Mostrar el resultado
    print("\n--- Resultados ---")
    print(f"Temperaturas registradas: {datos_temperaturas}")
    print(f"El promedio semanal del clima es: {promedio_semanal:.2f}")  # .2f para 2 decimales
    print("--- FIN: Programa de Promedio Semanal (Tradicional) ---\n")


# Ejecución del programa
if __name__ == "__main__":
    main_tradicional()