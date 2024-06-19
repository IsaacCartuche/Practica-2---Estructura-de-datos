import random
import sys
sys.path.append('../')

from CONTROLADOR.tda.linked.linkedList import Linked_List
from CONTROLADOR.DaoServidorPublicoControl import DaoServidorPublicoControl
from CONTROLADOR.DaoVentanillaControl import DaoVentanillaControl
from CONTROLADOR.DaoTransaccionControl import DaoTransaccionControl
################################################################################################
# BUSQUEDA
from CONTROLADOR.busqueda.binary import Binary
from CONTROLADOR.busqueda.binarySecuencial import BinarySecuencial

################################################################################################
# ORDENAMIENTO
from CONTROLADOR.ordenamiento.mergeSort import MergeSort
from CONTROLADOR.ordenamiento.quickSort import QuickSort
from CONTROLADOR.ordenamiento.shellSort import ShellSort

lista = Linked_List()

sp = DaoServidorPublicoControl()
vc = DaoVentanillaControl()
tc = DaoTransaccionControl()

try:

    
    """sp._servidorPublico._nombres = "Isaac"
    sp._servidorPublico._apellidos = "Cartuche"
    sp._servidorPublico._numeroPila = "001"
    sp.save
    
    
    sp._servidorPublico._nombres = "Ronald"
    sp._servidorPublico._apellidos = "Carderon"
    sp._servidorPublico._numeroPila = "002"
    sp.save
    
    sp._servidorPublico._nombres = "Godoy"
    sp._servidorPublico._apellidos = "Ronar"
    sp._servidorPublico._numeroPila = "003"
    sp.save"""
    
    
    
    # tc._transaccion._ventanilla = random.randint(1, 3)
    # tc._transaccion._fecha = "20/05/2024"
    # tc._transaccion._tiempo = random.uniform(5, 20)
    # tc._transaccion._detalle = "transacción diaria común"
    # tc._transaccion._calificacion = ""
    # tc.save
    

    # tc._transaccion._ventanilla = random.randint(1, 3)
    # tc._transaccion._fecha = "20/05/2024"
    # tc._transaccion._tiempo = random.uniform(5, 20)
    # tc._transaccion._detalle = "transacción diaria común"
    # tc._transaccion._calificacion = ""
    # tc.save
    
    # tc._transaccion._ventanilla = random.randint(1, 3)
    # tc._transaccion._fecha = "20/05/2024"
    # tc._transaccion._tiempo = random.uniform(5, 20)
    # tc._transaccion._detalle = "transacción diaria común"
    # tc._transaccion._calificacion = ""
    # tc.save
    
    # tc._transaccion._ventanilla = random.randint(1, 3)
    # tc._transaccion._fecha = "11/03/2024"
    # tc._transaccion._tiempo = random.uniform(5, 20)
    # tc._transaccion._detalle = "transacción diaria común"
    # tc._transaccion._calificacion = ""
    # tc.save
    
    # tc._transaccion._ventanilla = random.randint(1, 3)
    # tc._transaccion._fecha = "15/02/2024"
    # tc._transaccion._tiempo = random.uniform(5, 20)
    # tc._transaccion._detalle = "transacción diaria común"
    # tc._transaccion._calificacion = ""
    # tc.save
    
    # tc._transaccion._ventanilla = random.randint(1, 3)
    # tc._transaccion._fecha = "21/05/2024"
    # tc._transaccion._tiempo = random.uniform(5, 20)
    # tc._transaccion._detalle = "transacción diaria común"
    # tc._transaccion._calificacion = ""
    # tc.save
    
    # tc._transaccion._ventanilla = random.randint(1, 3)
    # tc._transaccion._fecha = "21/05/2024"
    # tc._transaccion._tiempo = random.uniform(5, 20)
    # tc._transaccion._detalle = "transacción diaria común"
    # tc._transaccion._calificacion = ""
    # tc.save
   
    # tc._transaccion._ventanilla = random.randint(1, 3)
    # tc._transaccion._fecha = "21/05/2024"
    # tc._transaccion._tiempo = random.uniform(5, 20)
    # tc._transaccion._detalle = "transacción diaria común"
    # tc._transaccion._calificacion = ""
    # tc.save
    
#     #print(tc.to_dict().__getitem__(0))
    
#     #print(tc.to_dict().__getitem__(0)['ventanilla'])ç
#     # print(type(tc.to_dict()))
#     # print(len(tc.to_dict()))
    
#     operacion ='1'
#     lista =tc.to_dict()
#     numero = len(lista)
#     #print(len(tc.to_dict()))
#     # while i < 6:
#     #     print("entra al for")
#     #     i += 1
        
            
            
            
            
    
#     while operacion != '0':
#         operacion = input("que ventanilla queire ver?")
#         fecha = input("que ventanilla queire ver? (20/05/2024 0 21/05/2024)")
#         i = int(0)
#         while i < numero:
            
#             if lista.__getitem__(i)['ventanilla'] == str(operacion) and lista.__getitem__(i)['fecha'] == str(fecha):
#                 print(float(lista.__getitem__(i)['tiempo']))
#             i += 1

        
        
        
#print(binary.search_binary(tc.lista.toArray(), ))
################################################################################
# METODOS DE ORDENAMIENTO
    
    #lista = sp._list()
    #lista.print
    # lista.sort_models("_apellidos", 1, 1)
    # lista.print
    
    
    
    
    #print(lista.toArray._array)
    #print(type(lista.toArray._array))
    #print(sp._get(15))
    #ms.sort_primitive_ascendent()
    
################################################################################
# METODOS DE BUSQUEDA
    
    
    # METODO SEARCH_BINARY_MODELS
    # lista = sp._list()
    #  #lista.print
    # print("#######################################################")
    # #    def search_binary_models(self, element, attribute):
    # attribute = "_apellidos"
    # index = lista.search_binary_models("cartuche", attribute)
    # lista = sp._list()
    # lista.sort_models(attribute, 1, 1)
    # print(lista.get(index).serialize)
    
    
    
    # # METODO SEARCH_BINARYSECUENCIAL_MODELS
    # lista = sp._list()
    # #lista.print
    # print("#######################################################")
    # # def search_binarySecuencial_models(self, element, attribute):
    # lista.search_binarySecuencial_models("cartuche", "_apellidos")
    # lista.print
    
    
    
    
    
except Exception as e:
    print(e)