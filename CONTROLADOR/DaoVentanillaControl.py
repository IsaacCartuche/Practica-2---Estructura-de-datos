from typing import Type
from CONTROLADOR.DAO.daoAdapter import DaoAdapter
from modelo.Ventanilla import Ventanilla

class DaoVentanillaControl(DaoAdapter):
    def __init__(self):
        super().__init__(Ventanilla)
        self.__ventanilla = None

    @property
    def _ventanilla(self):
        if self.__ventanilla == None:
            self.__ventanilla = Ventanilla()
        return self.__ventanilla

    @_ventanilla.setter
    def _ventanilla(self, value):
        self.__ventanilla = value

    @property
    def _lista(self):
        return self._list()
    
    