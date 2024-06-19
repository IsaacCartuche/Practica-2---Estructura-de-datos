class Transaccion:
    
    def __init__(self):
        self.__id = 0
        self.__ventanilla = None
        self.__fecha = ''
        self.__tiempo = None
        self.__detalle = ''
        self.__calificacion = ''

    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value
        
    @property
    def _ventanilla(self):
        return self.__ventanilla

    @_ventanilla.setter
    def _ventanilla(self, value):
        self.__ventanilla = value
    
    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value
    
    @property
    def _tiempo(self):
        return self.__tiempo

    @_tiempo.setter
    def _tiempo(self, value):
        self.__tiempo = value

    @property
    def _detalle(self):
        return self.__detalle

    @_detalle.setter
    def _detalle(self, value):
        self.__detalle = value

    @property
    def _calificacion(self):
        return self.__calificacion

    @_calificacion.setter
    def _calificacion(self, value):
        self.__calificacion = value
        
        
    @property
    def serialize(self):
        return {
            'id': self._id,
            'ventanilla': str(self._ventanilla),
            'fecha': self._fecha,
            'tiempo': str(self._tiempo),
            'detalle': self._detalle,
            'calificacion': self._calificacion
        }

    def deserializar(self, data):
        transaccion = Transaccion()
        transaccion._id = data['id']
        transaccion._ventanilla = data['ventanilla']
        transaccion._fecha = data['fecha']
        transaccion._tiempo = data['tiempo']
        transaccion._detalle = data['detalle']
        transaccion._calificacion = data['calificacion']
        return transaccion