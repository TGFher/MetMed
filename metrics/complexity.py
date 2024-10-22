import os
from radon.complexity import cc_rank, cc_visit


def measure_complexity(file_path):
    if not os.path.isfile(file_path):
        print("El archivo especificado no existe.")
        return

    with open(file_path, 'r') as file:
        code = file.read()

    results = cc_visit(code)
    for result in results:
        print(f"Nombre: {result.name}, Complejidad: {result.complexity}, Ranking: {cc_rank(result.complexity)}")
