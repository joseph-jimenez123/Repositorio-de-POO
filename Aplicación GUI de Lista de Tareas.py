import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas - Aplicación GUI")
        self.root.geometry("400x450")

        # --- Componentes de la Interfaz ---

        # Campo de entrada (Entry)
        self.task_entry = tk.Entry(root, font=("Arial", 12))
        self.task_entry.pack(pady=10, padx=20, fill=tk.X)

        # Vincular la tecla "Enter" para añadir tareas
        self.task_entry.bind('<Return>', lambda event: self.add_task())

        # Botones de acción
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task, bg="#4caf50", fg="white")
        self.add_button.pack(pady=5)

        # Lista de tareas (Listbox)
        self.tasks_listbox = tk.Listbox(root, font=("Arial", 12), selectmode=tk.SINGLE)
        self.tasks_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

        # Evento opcional: doble clic para marcar como completada
        self.tasks_listbox.bind('<Double-1>', lambda event: self.mark_completed())

        # Botones de gestión
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_completed, bg="#2196f3",
                                         fg="white")
        self.complete_button.pack(side=tk.LEFT, padx=25, pady=10)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task, bg="#f44336", fg="white")
        self.delete_button.pack(side=tk.RIGHT, padx=25, pady=10)

    # --- Lógica de la Aplicación ---

    def add_task(self):
        """Añade una nueva tarea a la lista."""
        task = self.task_entry.get()
        if task != "":
            self.tasks_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Debes escribir una tarea.")

    def mark_completed(self):
        """Cambia el estado visual de la tarea seleccionada."""
        try:
            index = self.tasks_listbox.curselection()[0]
            task = self.tasks_listbox.get(index)

            # Si ya está completada (ej. tiene el check), no hacemos nada o avisamos
            if "✔" not in task:
                completed_task = f"{task} ✔"
                self.tasks_listbox.delete(index)
                self.tasks_listbox.insert(index, completed_task)
                self.tasks_listbox.itemconfig(index, fg="gray")  # Cambio visual de color
            else:
                messagebox.showinfo("Info", "La tarea ya está marcada como completada.")
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar.")

    def delete_task(self):
        """Remueve la tarea seleccionada de la lista."""
        try:
            index = self.tasks_listbox.curselection()[0]
            self.tasks_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
