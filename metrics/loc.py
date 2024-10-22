import os


def measure_loc(file_path):
    if not os.path.isfile(file_path):
        print("El archivo especificado no existe.")
        return

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Contar líneas de código excluyendo las vacías y los comentarios
    code_lines = [line for line in lines if line.strip() and not line.strip().startswith("#")]
    total_lines = len(lines)
    code_lines_count = len(code_lines)

    print(f"Total de Líneas: {total_lines}")
    print(f"Líneas de Código (excluyendo comentarios y líneas vacías): {code_lines_count}")
