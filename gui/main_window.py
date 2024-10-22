# Importar las librerías necesarias
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from metrics.complexity import measure_complexity
from metrics.loc import measure_loc
from metrics.test_coverage import measure_coverage

# Clase para la Ventana Principal
def main_window():
    # Crear la ventana principal
    root = tk.Tk()
    root.title("Software Metrics Application")
    root.geometry("700x600")
    root.configure(bg="#f0f4f8")  # Color de fondo suave
    root.resizable(False, False)

    # Función para mostrar la bienvenida y las instrucciones
    def mostrar_bienvenida():
        messagebox.showinfo("Bienvenida", "Bienvenido a la Aplicación de Métricas de Software.\n\nInstrucciones:\n- Seleccione 'Medir Complejidad Ciclomática' para calcular la complejidad del código.\n- Seleccione 'Medir Líneas de Código' para contar las líneas de código.\n- Seleccione 'Medir Cobertura de Pruebas' para medir la cobertura de pruebas del proyecto.")

    # Mostrar la bienvenida al inicio
    mostrar_bienvenida()

    # Título
    title_label = ttk.Label(root, text="Aplicación de Métricas de Software", font=("Helvetica", 22, "bold"), foreground="#2c3e50", background="#f0f4f8")
    title_label.pack(pady=20)

    # Frame para los botones
    button_frame = ttk.Frame(root, padding=20, style="TFrame")
    button_frame.pack(expand=True)

    # Estilo de los botones y el frame
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 14), padding=10, background="#ffffff")
    style.configure("TFrame", background="#f0f4f8")

    # Función para seleccionar archivo y medir complejidad
    def medir_complejidad():
        file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Python Files", "*.py")])
        if file_path:
            measure_complexity(file_path)
            messagebox.showinfo("Éxito", "La complejidad ciclomatica ha sido medida correctamente.")

    # Función para seleccionar archivo y medir líneas de código
    def medir_loc():
        file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[("Python Files", "*.py")])
        if file_path:
            measure_loc(file_path)
            messagebox.showinfo("Éxito", "Las líneas de código han sido contadas correctamente.")

    # Función para seleccionar directorio y medir cobertura de pruebas
    def medir_cobertura():
        directory_path = filedialog.askdirectory(title="Seleccionar directorio de proyecto")
        if directory_path:
            measure_coverage(directory_path)
            messagebox.showinfo("Éxito", "La cobertura de pruebas ha sido medida correctamente.")

    # Crear botones y ubicarlos en el frame de botones
    complexity_button = ttk.Button(button_frame, text="Medir Complejidad Ciclomática", command=medir_complejidad)
    complexity_button.grid(row=0, column=0, padx=20, pady=20)

    loc_button = ttk.Button(button_frame, text="Medir Líneas de Código (LOC)", command=medir_loc)
    loc_button.grid(row=0, column=1, padx=20, pady=20)

    coverage_button = ttk.Button(button_frame, text="Medir Cobertura de Pruebas", command=medir_cobertura)
    coverage_button.grid(row=1, column=0, columnspan=2, pady=20)

    # Iniciar el bucle principal de la interfaz
    root.mainloop()

# Ejecutar la ventana principal si este archivo se ejecuta directamente
if __name__ == "__main__":
    main_window()
