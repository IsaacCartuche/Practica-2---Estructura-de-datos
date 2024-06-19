from CONTROLADOR.tda.linked.node import Node
from CONTROLADOR.exception.linkedListExeption import LinkedEmpty
from CONTROLADOR.exception.arrayPositionException import ArrayPositionException
from CONTROLADOR.exception.linkedListExeption import LinkedEmpty
from CONTROLADOR.tdaArray import TDAArray
from numbers import Number

#######################################################################################################
### METODOS DE ORDENAMIENTO
from CONTROLADOR.ordenamiento.mergeSort import MergeSort
from CONTROLADOR.ordenamiento.quickSort import QuickSort
from CONTROLADOR.ordenamiento.shellSort import ShellSort
#######################################################################################################
### METODOS DE busqueda
from CONTROLADOR.busqueda.binary import Binary
from CONTROLADOR.busqueda.binarySecuencial import BinarySecuencial



class Linked_List(object):
    def __init__(self):
        self.__head = None
        self.__last = None
        self.__length = 0
        
    @property
    def _length(self):
        return self.__length

    @_length.setter
    def _length(self, value):
        self.__length = value


    @property
    def isEmpty(self):
        return self.__head == None or self.__length == 0
    
    def __addFirst__(self, data):
        if self.isEmpty:
            node = Node(data)
            self.__head = node
            self.__last = node
            self.__length += 1
        else: 
            headOld = self.__head
            self.__head = Node(data, headOld)
            self.__length += 1

    def __addLast__(self, data):
            if self.isEmpty:
                self.__addFirst__(data)
            else: 
                node = Node(data)
                self.__last._next = node
                self.__last = node
                self.__length += 1

    def edit(self, data, pos=0):
        if pos == 0:
            self.__head._data = data
        elif pos == self._length:
            self.__last._data = data
        else:
            self.getNode(pos)._data = data
                   
    
    def getNode(self, pos):
        if self.isEmpty:
            #raise LinkedEmpty("List is Empty")
            print("List Empty")
        elif pos < 0 or pos >= self._length:
            #raise ArrayPositionException("Position is out of range")
            print("Position is out of range")
        elif pos == 0:
            return self.__head
        elif pos == self._length -1 :
            return self.__last
        else:
            count = 0
            node = self.__head
            while count < pos:
                node = node._next
                count += 1
            return node
        
    def get(self, pos):
        return self.getNode(pos)._data
        

    def add(self, data, pos = 0):
        if self.isEmpty:
            self.__addFirst__(data)
        elif pos == self._length:
            self.__addLast__(data)
        else:
            node_preview = self.getNode(pos-1)
            node_last = node_preview._next
            node_preview._next = Node(data, node_last)
            self.__length += 1
    
    
    @property
    def clear(self):
        self.__head = None
        self.__last = None
        self.__length = 0


    @property    
    def toArray(self):
        # print("primera prueba")
        # out = []
        # print("segunda prueba")
        # if self.isEmpty:
            
        #     out = "List is Empty"
        # else:
        #     print("tercera prueba")
        #     node = self.__head
        #     print("cuarta prueba")
        #     while node!= None:
        #         print("quinta prueba")
        #         out.append(node._data.__name)
        #         print("sexta prueba")
        #         node = node._next

        # return out
        array = TDAArray(self._length)
        if not self.isEmpty:
            node = self.__head
            cont = 0
            while cont < self._length:
                #array.insert(node._data, cont)
                #print(node._data.serialize)
                #print(node)
                array.insert(node._data, cont)
                cont += 1
                node = node._next
        
        return array
    
    def detele(self, pos=0):
        #TODO
        pass
    
    def __str__(self) -> str:
        out = ""
        if self.isEmpty:
            out = "List is Empty"
        else:
            node = self.__head
            while node!= None:
                out += str(node._data) +'\t'
                node = node._next
        return out
    
    def toList(self, array):
        self.clear
        for i in range (0, len(array)):
            self.__addLast__(array[i])

    @property
    def print(self):
        
        node = self.__head
        data = ""
        while node != None:
            data += str(node._data)
            node = node._next
        print("Lista de datos")
        print(data)
        return data
    
#######################################################################################################
### METODOS DE ORDENAMIENTO
    
    #Ordenamiento de la lista-------------------------------------------------------------------------------------------------
    def sort(self, type, metodo = 1):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray._array
            if isinstance(array[0], Number) or isinstance(array[0], str):
                if metodo == 1:
                    order = QuickSort()
                elif metodo == 2:
                    order = MergeSort()
                else:
                    order = ShellSort()
                if type == 1:
                    array = order.sort_primitive_ascendent(array)
                else:
                    array = order.sort_primitive_descendent(array)
            self.toList(array)

    def sort_models(self, attribute, type = 1, metodo = 1):
        if self.isEmpty:
            #raise LinkedEmpty("List empty")
            print("lista Vacia")
        else:
            array = self.toArray._array
            
            if isinstance(array[0], object):
                if metodo == 1:
                    order = QuickSort()
                elif metodo == 2:
                    order = MergeSort()
                else:
                    order = ShellSort()
                if type == 1:
                    array = order.sort_models_ascendent(array, attribute)
                else:
                    array = order.sort_models_descendent(array, attribute)
            
            self.toList(array)
        return self

#######################################################################################################
### METODOS DE BUSQUEDA

    def search_equals(self, data):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray._array
            for i in range(0, len(array)):
                if array[i] == data: #array[i].lower().startswith(data.lower()): #:
                    list.add(array[i], list._length)
        return list

    def search_equals_number(self, number):
        list = Linked_List()
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray._array
            for i in range(len(array)):
                if array[i] == number:
                    list.add(array[i], list._lenght)
            #imprimir el numero de ocurrencia que se encontraron
            #print(f"El número {number} fue encontrado {list._lenght} veces")
        return list

        
    #--------------------------Binario------------------------------------------------------------------------------------------------
        
    def search_binary(self, element):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray._array
            search = Binary()
            index = search.search_binary(array, element)
            if index == -1:
                print(f"Elemento {element} no encontrado")
            else:
                print(f"Elemento {element} encontrado en el índice: {index}")
            
        self.toList(array)
        return self

    def search_binary_models(self, element, attribute):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray._array
            
            search = Binary()
            quickSort = QuickSort()
            array = quickSort.sort_models_ascendent(array, attribute)
            #array = quickSort.sort_models_descendent(array, attribute)
            index = search.search_binary_models(array, element, attribute)
            
            if index == -1:
                print(f"Models con {attribute} = {element} no encontrado")
            else:
                print(f"Models con {attribute} = {element} encontrado en el objeto: {index}")
        
        self.toList(array)
        #return self
        return index

    #--------------------------Binario Secuencial------------------------------------------------------------------------------------------------
    def search_binarySecuencial(self, element):
        if self.isEmpty:
            raise LinkedEmpty("List empty")
        else:
            array = self.toArray._array
            search = BinarySecuencial()
            index = search.search_BinarySecuencial(array, element)
            if index == -1:
                print(f"Elemento {element} no encontrado")
            else:
                print(f"Elemento {element} fue encontrado en estas ocasiones: {index}")
            
        self.toList(array)
        return self

    def search_binarySecuencial_models(self, element, attribute):
        if self.isEmpty:
            #raise LinkedEmpty("List empty")
            print("List empty")
        else:
                
            array = self.toArray._array
            search = BinarySecuencial()
            quickSort = QuickSort()
            array = quickSort.sort_models_ascendent(array, attribute)
            index = search.search_BinarySecuencial_models(array, element, attribute)
            
            #print(index)
            aux = []
            if index == -1:
                print(f"Models con {attribute} = {element} no encontrado")
                
            else:
                print(f"los modelos con {attribute} = {element} fueron encontrados en:") #{index}
                
                for i in range(0, len(index)):
                    aux.append(index[i].serialize)
        
        self.toList(aux)