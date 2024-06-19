from typing import Type
from CONTROLADOR.DAO.daoAdapter import DaoAdapter
from modelo.ServidorPublico import ServidorPublico

class DaoServidorPublicoControl(DaoAdapter):
    def __init__(self):
        super().__init__(ServidorPublico)
        self.__servidorPublico = None 

    @property
    def _servidorPublico(self):
        if self.__servidorPublico == None:
            self.__servidorPublico = ServidorPublico()
        return self.__servidorPublico

    @_servidorPublico.setter
    def _servidorPublico(self, value):
        self.__servidorPublico = value

    @property
    def _lista(self):
        return self._list()

    @property
    def save(self):
        self.__servidorPublico._id = self._lista._length + 1
        #print('Servidor publico dao control:')
        #print(self.__servidorPublico.serialize)
        self._save(self.__servidorPublico)    
    
    def merge(self, pos):
        self._merge(self.__servidorPublico, pos)