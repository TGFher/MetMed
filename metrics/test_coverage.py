import os
import subprocess

def measure_coverage(directory_path):
    if not os.path.isdir(directory_path):
        print("El directorio especificado no existe.")
        return

    try:
        # Ejecutar el comando de cobertura
        subprocess.run(["coverage", "run", "--source", directory_path, "-m", "unittest", "discover"], check=True)
        subprocess.run(["coverage", "report"], check=True)
    except subprocess.CalledProcessError as e:
        print("Hubo un error al medir la cobertura de pruebas:", e)
