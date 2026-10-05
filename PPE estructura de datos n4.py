import heapq
import time

class GrafoVuelos:
    def __init__(self):
        self.grafo = {}

    def cargar_desde_archivo(self, ruta_archivo):
        try:
            with open(ruta_archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea or linea.startswith('#'):
                        continue
                    partes = [p.strip() for p in linea.split(',')]
                    if len(partes) == 6:
                        id_vuelo, origen, destino, costo, duracion, escalas = partes
                        self.agregar_conexion(origen, destino, float(costo), float(duracion))
            print("[INFO] Base de datos de vuelos cargada exitosamente en memoria.")
        except FileNotFoundError:
            print(f"[ERROR] No se encontró el archivo en la ruta: {ruta_archivo}")

    def agregar_conexion(self, origen, destino, costo, duracion):
        if origen not in self.grafo:
            self.grafo[origen] = []
        self.grafo[origen].append((destino, costo, duracion))

    def buscar_ruta_mas_barata(self, inicio, fin):
        # Cola de prioridad: (costo_acumulado, duracion_acumulada, nodo_actual, camino)
        cola_prioridad = [(0.0, 0.0, inicio, [inicio])]
        visitados = set()

        inicio_tiempo = time.time()

        while cola_prioridad:
            costo_actual, duracion_actual, nodo_actual, camino = heapq.heappop(cola_prioridad)

            if nodo_actual == fin:
                tiempo_ejecucion = (time.time() - inicio_tiempo) * 1000
                return costo_actual, duracion_actual, camino, tiempo_ejecucion

            if nodo_actual in visitados:
                continue
            visitados.add(nodo_actual)

            if nodo_actual in self.grafo:
                for vecino, costo, duracion in self.grafo[nodo_actual]:
                    if vecino not in visitados:
                        heapq.heappush(cola_prioridad, (
                            costo_actual + costo,
                            duracion_actual + duracion,
                            vecino,
                            camino + [vecino]
                        ))
        return None, None, [], 0.0

# Bloque de ejecución principal de pruebas
if __name__ == "__main__":
    sistema = GrafoVuelos()
    # Simulación de carga y consulta
    sistema.cargar_desde_archivo("vuelos_db.txt")
    costo, duracion, ruta, t_ejec = sistema.buscar_ruta_mas_barata("UIO", "MAD")
    print(f"Ruta óptima encontrada: {' -> '.join(ruta)}")
    print(f"Costo Total: ${costo:.2f} USD | Duración: {duracion} hrs | Tiempo de cálculo: {t_ejec:.4f} ms")