from typing import Type
from CONTROLADOR.DAO.daoAdapter import DaoAdapter
from modelo.transaccion import Transaccion

class DaoTransaccionControl(DaoAdapter):
    def __init__(self):
        super().__init__(Transaccion)
        self.__transaccion = None

    @property
    def _transaccion(self):
        if self.__transaccion == None:
            self.__transaccion = Transaccion()
        return self.__transaccion

    @_transaccion.setter
    def _transaccion(self, value):
        self.__transaccion = value

    @property
    def _lista(self):
        return self._list()
    
    @property
    def save(self):
        self.__transaccion._id = self._lista._length + 1
        # print('Transaccion Dao control:')
        # print(self.__transaccion.serialize)
        self._save(self.__transaccion)    
    
    def merge(self, pos):
        self._merge(self.__transaccion, pos)
