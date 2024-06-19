class ServidorPublico():
    def __init__(self):
        self.__id = 0
        self.__nombres = None
        self.__apellidos = None
        self.__numeroPila = None

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value
    
    @property
    def _nombres(self):
        return self.__nombres

    @_nombres.setter
    def _nombres(self, value):
        self.__nombres = value

    @property
    def _apellidos(self):
        return self.__apellidos

    @_apellidos.setter
    def _apellidos(self, value):
        self.__apellidos = value

    @property
    def _numeroPila(self):
        return self.__numeroPila

    @_numeroPila.setter
    def _numeroPila(self, value):
        self.__numeroPila = value
    
    @property
    def serialize(self):
        return {
            'id': self._id,
            'nombres': self._nombres,
            'apellidos': self._apellidos,
            'numeroPila': self._numeroPila
        }

    def __str__(self):
        return f'{self.__id} {self.__apellidos} {self.__nombres} {self.__numeroPila}'
    
    
    def deserializar(self, data):
        servidorPublico = ServidorPublico()
        servidorPublico._id = data['id']
        servidorPublico._nombres = data['nombres']
        servidorPublico._apellidos = data['apellidos']
        servidorPublico._numeroPila = data['numeroPila']
        return servidorPublico
    
    