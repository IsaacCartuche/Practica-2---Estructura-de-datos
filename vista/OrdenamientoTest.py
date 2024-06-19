import random
import time
import sys
sys.path.append('../')

# Importación de la clase ShellSort, MergeSort y QuickSort
from CONTROLADOR.ordenamiento.shellSort import ShellSort
from CONTROLADOR.ordenamiento.mergeSort import MergeSort
from CONTROLADOR.ordenamiento.quickSort import QuickSort


# Generación de un arreglo aleatorio de 10000 elementos
arr = [random.randint(1, 25000) for _ in range(25000)]

# Instanciación de ShellSort
shell_sort_instance = ShellSort()

# Instanciación de MergeSort
merge_sort_instance = MergeSort()

# Instanciación de QuickSort
quick_sort_instance = QuickSort()

# Función para medir el tiempo de ejecución de un algoritmo de ordenamiento
def measure_sorting_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr.copy())  # Usamos .copy() para no alterar el arreglo original
    return time.time() - start_time

# Medición del tiempo para Shell Sort
shell_sort_time = measure_sorting_time(shell_sort_instance.sort_primitive_ascendent, arr.copy())

# Medición del tiempo para Merge Sort
merge_sort_time = measure_sorting_time(merge_sort_instance.sort_primitive_ascendent, arr.copy())

# Medición del tiempo para QuickSort
quick_sort_time = measure_sorting_time(quick_sort_instance.sort_primitive_ascendent, arr.copy())

# Imprimir los tiempos de ejecución
print(f"Tiempo de ejecución de Shell Sort (ascendente): {shell_sort_time} segundos")
print(f"Tiempo de ejecución de Merge Sort (ascendente): {merge_sort_time} segundos")
print(f"Tiempo de ejecución de QuickSort (ascendente): {quick_sort_time} segundos")