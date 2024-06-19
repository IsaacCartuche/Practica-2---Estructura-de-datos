import random
import time

class Secuencial:
    def search_sequential_primitive(self, array, element):
        for i in range(len(array)):
            if array[i] == element:
                return i
        return -1

    def search_sequential(self, array, element, index):
        left = index
        right = index
        while left > 0 and array[left - 1] == element:
            left -= 1
        while right < len(array) - 1 and array[right + 1] == element:
            right += 1
       
        return array[left:right + 1]
    
    def search_sequential_models(self, array, element, attribute, index):
        element = element.upper()
        left = index
        right = index
        while left > 0 and getattr(array[left - 1], attribute).upper() == element:
            left -= 1
        while right < len(array) - 1 and getattr(array[right + 1], attribute).upper() == element:
            right += 1
        
        return array[left:right + 1]

# Implementación de la clase BinarySecuencial (binarySecuencial.py)
class BinarySecuencial:
    def search_BinarySecuencial(self, array, element):
        sorted_array = sorted(array)
        index = self.binary_search(sorted_array, element)
        if index == -1:
            return -1
        
        secuencial = Secuencial()
        return secuencial.search_sequential(sorted_array, element, index)
    
    def binary_search(self, array, element):
        left = 0
        right = len(array) - 1
        while left <= right:
            mid = (left + right) // 2
            if array[mid] == element:
                return mid
            elif array[mid] < element:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# Función para generar un arreglo de tamaño dado con números aleatorios únicos
def generar_arreglo(tamano):
    return random.sample(range(1, 1000000), tamano)

# Función para medir el tiempo de búsqueda secuencial
def medir_tiempo_secuencial(arreglo, elemento_a_buscar):
    secuencial = Secuencial()
    inicio = time.time()
    secuencial.search_sequential_primitive(arreglo, elemento_a_buscar)
    fin = time.time()
    return (fin - inicio) * 1000  # Convertir a milisegundos

# Función para medir el tiempo de búsqueda binaria
def medir_tiempo_binario(arreglo, elemento_a_buscar):
    binary_secuencial = BinarySecuencial()
    inicio = time.time()
    binary_secuencial.search_BinarySecuencial(arreglo, elemento_a_buscar)
    fin = time.time()
    return (fin - inicio) * 1000  # Convertir a milisegundos

# Función para ejecutar las mediciones y registrar los tiempos en una tabla
def ejecutar_medicion_y_registrar(tamano_arreglo):
    arreglo = generar_arreglo(tamano_arreglo)
    elemento_a_buscar = arreglo[-1]  # Buscar el último elemento del arreglo
    
    tiempo_secuencial = medir_tiempo_secuencial(arreglo, elemento_a_buscar)
    tiempo_binario = medir_tiempo_binario(arreglo, elemento_a_buscar)
    
    return {
        'Tamaño del arreglo': tamano_arreglo,
        'Tiempo secuencial (ms)': tiempo_secuencial,
        'Tiempo binario (ms)': tiempo_binario
    }

# Tamaños de arreglos a generar y medir
tamanos_arreglos = [25000]

# Realizar las mediciones para cada tamaño de arreglo
resultados = []
for tamano_arreglo in tamanos_arreglos:
    resultado_medicion = ejecutar_medicion_y_registrar(tamano_arreglo)
    resultados.append(resultado_medicion)

# Imprimir resultados en forma de tabla
print("\nResultados de las mediciones de tiempo:")
print("=======================================")
print("| Tamaño del arreglo | Tiempo secuencial (ms) | Tiempo Lineal binario (ms) |")
print("------------------------------------------------------------------")
for resultado in resultados:
    print(f"| {resultado['Tamaño del arreglo']:18} | {resultado['Tiempo secuencial (ms)']:23.3f} | {resultado['Tiempo binario (ms)']:19.3f} |")
print("==================================================================")