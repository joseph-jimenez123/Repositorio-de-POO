import os


class Paciente:
    def __init__(self, cedula: str, nombre: str, edad: int):
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad


class Turno:
    def __init__(self, codigo_turno: int):
        self.codigo_turno = codigo_turno
        self.paciente = None  # None significa que el turno está [LIBRE]
        self.esta_asignado = False


class GestionAgenda:
    def __init__(self):
        self.MAX_BLOQUES = 8  # 8 horas de jornada laboral (0 a 7)
        self.MAX_ESPECIALIDADES = 3  # 0: Pediatría, 1: Cardiología, 2: Med. General
        # Inicialización matricial estática (Lista de listas)
        self.matriz_agenda = [[Turno(0) for _ in range(self.MAX_ESPECIALIDADES)] for _ in range(self.MAX_BLOQUES)]
        self.inicializar_codigos()

    def inicializar_codigos(self):
        # Asigna un código secuencial fijo a cada celda de la agenda
        codigo = 101
        for f in range(self.MAX_BLOQUES):
            for c in range(self.MAX_ESPECIALIDADES):
                self.matriz_agenda[f][c].codigo_turno = codigo
                codigo += 1

    def registrar_turno(self, bloque: int, especialidad: int, paciente: Paciente) -> bool:
        if 0 <= bloque < self.MAX_BLOQUES and 0 <= os.sys.maxsize:  # Control de límites
            if 0 <= especialidad < self.MAX_ESPECIALIDADES:
                turno = self.matriz_agenda[bloque][especialidad]
                if not turno.esta_asignado:
                    turno.paciente = paciente
                    turno.esta_asignado = True
                    return True
        return False

    def mostrar_agenda(self):
        especialidades = ["Pediatría", "Cardiología", "Med. General"]
        horas = ["08:00", "09:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00"]

        print("\n" + "=" * 85)
        print(f"{'HORA':<10} | {'PEDIATRÍA':<22} | {'CARDIOLOGÍA':<22} | {'MED. GENERAL':<22}")
        print("=" * 85)

        for f in range(self.MAX_BLOQUES):
            fila_str = f"{horas[f]:<10} | "
            for c in range(self.MAX_ESPECIALIDADES):
                turno = self.matriz_agenda[f][c]
                if turno.esta_asignado:
                    info = f"{turno.paciente.nombre} (ID:{turno.codigo_turno})"
                else:
                    info = f"[LIBRE] (ID:{turno.codigo_turno})"
                fila_str += f"{info:<22} | "
            print(fila_str)
        print("=" * 85)


# Bloque de ejecución principal con menú interactivo
if __name__ == "__main__":
    sistema = GestionAgenda()

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE TURNOS - CLÍNICA SALUD AMAZÓNICA ---")
        print("1. Registrar nuevo turno")
        print("2. Visualizar reporte de agenda completa (Reportería)")
        print("3. Salir del sistema")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            print("\n--- REGISTRO DE PACIENTE ---")
            cedula = input("Ingrese cédula del paciente: ")
            nombre = input("Ingrese nombres completos: ")
            try:
                edad = int(input("Ingrese edad: "))

                print("\nBloques Horarios disponibles:")
                print("0: 08:00 | 1: 09:00 | 2: 10:00 | 3: 11:00\n4: 12:00 | 5: 14:00 | 6: 15:00 | 7: 16:00")
                bloque = int(input("Seleccione el número de bloque (0-7): "))

                print("\nEspecialidades disponibles:")
                print("0: Pediatría | 1: Cardiología | 2: Medicina General")
                especialidad = int(input("Seleccione el número de especialidad (0-2): "))

                nuevo_paciente = Paciente(cedula, nombre, edad)
                exito = sistema.registrar_turno(bloque, especialidad, nuevo_paciente)

                if exito:
                    print("\n[ÉXITO] Turno asignado correctamente.")
                else:
                    print("\n[ERROR] El bloque seleccionado ya está ocupado o los índices son inválidos.")
            except ValueError:
                print("\n[ERROR] Datos de entrada inválidos. Intente de nuevo.")

        elif opcion == "2":
            sistema.mostrar_agenda()

        elif opcion == "3":
            print("\nFinalizando el sistema. Guardando registros en memoria estática...")
            break
        else:
            print("\n[ERROR] Opción no válida.")