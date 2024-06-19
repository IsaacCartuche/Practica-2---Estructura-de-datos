from CONTROLADOR.tda.linked import linkedList
from CONTROLADOR.DaoServidorPublicoControl import DaoServidorPublicoControl
from CONTROLADOR.DaoTransaccionControl import DaoTransaccionControl

class Ventanilla:
    def __init__(self):
        self.__numero = None
        self.__transacciones = DaoTransaccionControl()
        self.__servidor = DaoServidorPublicoControl()

    @property
    def _numero(self):
        return self.__numero

    @_numero.setter
    def _numero(self, value):
        self.__numero = value

    @property
    def _transacciones(self):
        return self.__transacciones

    @_transacciones.setter
    def _transacciones(self, value):
        self.__transacciones = value

    @property
    def _servidor(self):
        return self.__servidor

    @_servidor.setter
    def _servidor(self, value):
        self.__servidor = value
