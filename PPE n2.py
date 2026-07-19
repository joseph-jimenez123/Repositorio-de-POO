import time
from datetime import datetime


# ==============================================================================
# ENTIDAD DE DOMINIO: PERSONA
# ==============================================================================
class Persona:
    """
    Representa a un usuario individual que ingresa a la línea de espera.
    Encapsula los datos básicos exigidos para el control de la atracción.
    """

    def __init__(self, id_usuario: int, nombre: str):
        self.__id = id_usuario
        self.__nombre = nombre
        # Captura el instante exacto con precisión de milisegundos
        self.__hora_llegada = datetime.now().strftime("%H:%M:%S.%f")[:-3]

    @property
    def id(self) -> int:
        return self.__id

    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def hora_llegada(self) -> str:
        return self.__hora_llegada

    def __str__(self) -> str:
        return f"[ID: {self.__id:02d}] | Pasajero: {self.__nombre:<12} | Llegada: {self.__hora_llegada}"


# ==============================================================================
# ESTUCTURA LÓGICA: NODO DE MEMORIA
# ==============================================================================
class Nodo:
    """
    Componente estructural primitivo para la construcción de la cola dinámica.
    Evita el uso de vectores indexados fijos, permitiendo un manejo eficiente.
    """

    def __init__(self, persona: Persona):
        self.persona = persona
        self.siguiente = None


# ==============================================================================
# TIPO ABSTRACTO DE DATOS (TAD): COLA DINÁMICA
# ==============================================================================
class ColaAtraccion:
    """
    Implementación formal del TAD Cola bajo la política FIFO (First In, First Out).
    Restringe perimetralmente la capacidad máxima a 30 elementos.
    """

    def __init__(self, capacidad_maxima: int = 30):
        self.__frente = None
        self.__final = None
        self.__contador_elementos = 0
        self.__capacidad_maxima = capacidad_maxima

    def esta_vacia(self) -> bool:
        return self.__frente is None

    @property
    def contador(self) -> int:
        return self.__contador_elementos

    @property
    def capacidad_maxima(self) -> int:
        return self.__capacidad_maxima

    def encolar(self, persona: Persona) -> bool:
        """
        Inserta un elemento al final de la cola (Operación Enqueue).
        Complejidad Temporal: O(1).
        """
        # Validación perimetral estricta solicitada en la guía de prácticas
        if self.__contador_elementos >= self.__capacidad_maxima:
            print(
                f" [RECHAZADO] -> Imposible encolar a {persona.nombre}. Límite de {self.__capacidad_maxima} asientos agotado.")
            return False

        nuevo_nodo = Nodo(persona)
        if self.esta_vacia():
            self.__frente = nuevo_nodo
            self.__final = nuevo_nodo
        else:
            self.__final.siguiente = nuevo_nodo
            self.__final = nuevo_nodo

        self.__contador_elementos += 1
        return True

    def desencolar(self) -> Persona:
        """
        Remueve y extrae el elemento del frente de la cola (Operación Dequeue).
        Complejidad Temporal: O(1).
        """
        if self.esta_vacia():
            raise IndexError("Desbordamiento inferior (Underflow): La cola está vacía.")

        nodo_extraido = self.__frente
        self.__frente = self.__frente.siguiente

        if self.__frente is None:
            self.__final = None

        self.__contador_elementos -= 1
        return nodo_extraido.persona

    def consultar_frente(self) -> Persona:
        """
        Inspecciona el elemento inicial sin alterar la estructura (Operación Peek).
        Complejidad Temporal: O(1).
        """
        if self.esta_vacia():
            return None
        return self.__frente.persona

    def generar_reporte_consola(self):
        """
        Recorre linealmente la estructura para visualizar el estado de la cola
        en cumplimiento con los requerimientos de reportería del docente.
        """
        print("\n" + "=" * 75)
        print(
            f" AUDITORÍA DE ASIGNACIÓN: LÍNEA DE ESPERA ({self.__contador_elementos}/{self.__capacidad_maxima} ASENTOS)")
        print("=" * 75)
        if self.esta_vacia():
            print(" No existen usuarios registrados en la cola actual.")
            return

        actual = self.__frente
        posicion = 1
        while actual is not None:
            print(f" Posición {posicion:02d} En Fila -> {actual.persona}")
            actual = actual.siguiente
            posicion += 1
        print("=" * 75)


# ==============================================================================
# PROGRAMA PRINCIPAL / GESTOR DE LA SIMULACIÓN
# ==============================================================================
if __name__ == "__main__":
    print("=== UNIVERSIDAD ESTATAL AMAZÓNICA ===")
    print("Iniciando Simulador Práctico: Estructuras de Datos Lineales (Colas)\n")

    # Inicialización del TAD con la restricción perimetral del problema
    fila_atraccion = ColaAtraccion(capacidad_maxima=30)

    # Nómina de pasajeros aleatorios para llenar la capacidad exacta del sistema
    pasajeros_simulados = [
        "Carlos", "Ana", "Luis", "Maria", "Jorge", "Elena", "Pedro", "Sofia", "Juan", "Lucia",
        "Diego", "Laura", "Andres", "Paula", "Miguel", "Marta", "Gabriel", "Valentina", "Jose", "Camila",
        "Manuel", "Isabella", "Mateo", "Victoria", "David", "Ximena", "Alejandro", "Daniela", "Javier", "Natalia"
    ]

    # --------------------------------------------------------------------------
    # FASE 1: INSERCIÓN SECUENCIAL (ENQUEUE) Y MEDICIÓN DE TIEMPO
    # --------------------------------------------------------------------------
    print("[FASE 1] Registrando pasajeros en orden cronológico de llegada...")

    # Alta precisión para el cálculo del rendimiento algorítmico
    inicio_reloj = time.perf_counter()

    for indice, nombre in enumerate(pasajeros_simulados):
        nuevo_visitante = Persona(id_usuario=indice + 1, nombre=nombre)
        fila_atraccion.encolar(nuevo_visitante)
        time.sleep(0.005)  # Simula un pequeño retraso físico en milisegundos

    fin_reloj = time.perf_counter()
    tiempo_total_ms = (fin_reloj - inicio_reloj) * 1000

    # Intento de inserción número 31 para verificar el control de desbordamiento (Overflow)
    pasajero_excedente = Persona(id_usuario=31, nombre="Roberto")
    fila_atraccion.encolar(pasajero_excedente)

    # --------------------------------------------------------------------------
    # FASE 2: VISUALIZACIÓN Y CONSULTA (REPORTERÍA)
    # --------------------------------------------------------------------------
    fila_atraccion.generar_reporte_consola()
    print(f"MÉTRICA DE RENDIMIENTO: Tiempo total de encolado masivo: {tiempo_total_ms:.4f} ms")

    # --------------------------------------------------------------------------
    # FASE 3: DESPACHO Y ABORDAJE DE LA ATRACCIÓN (DEQUEUE)
    # --------------------------------------------------------------------------
    print("\n[FASE 3] Capacidad máxima completada. Iniciando abordaje del juego mecánico...")

    # Demostración del método Peek (Inspección previa)
    proximo_a_subir = fila_atraccion.consultar_frente()
    if proximo_a_subir:
        print(f" Verificación de Entrada: El primer usuario en abordar será: {proximo_a_subir.nombre}")

    print("\nProcesando asientos vendidos en estricto orden FIFO:")
    print("-" * 50)
    while not fila_atraccion.esta_vacia():
        pasajero_atendido = fila_atraccion.desencolar()
        print(f" [ASIENTO ASIGNADO] -> {pasajero_atendido.nombre} ha ingresado a la atracción.")

    print("-" * 50)
    print("Simulación Concluida: La cola se ha vaciado. Todos los asientos fueron ocupados correctamente.")

