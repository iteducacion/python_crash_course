
from datetime import date


class Gasto():
    """Clase que representa un gasto"""

    def __init__(self, type = '', date = date.today(), total = 0):
        """Inicializa los atributos"""
        self.type   = type
        self.date   = date
        self.total  = total
    
    def get_type(self):
        """Devuelve el tipo de gasto"""
        return self.type
    
    def get_date(self):
        """Devuelve la fecha del gasto"""
        return self.date

    def get_total(self):
        """Devuelve el total del gasto"""
        return self.total
    
    def set_type(self, type):
        """Modifica el tipo de gasto"""
        self.type = type
    
    def set_date(self, date):
        """Modifica la fecha del gasto"""
        self.date = date
    
    def set_total(self, total):
        """Modifica el total del gasto"""
        self.total = total
    

    def show(self):
        """Muestra los datos del gasto"""
        print('Gasto -----> ' + ' Tipo de Gasto: ' + self.type + ' - Fecha: ' + str(self.date) + ' - Total: ' + str(self.total))

    def aplicar_gasto_en_planilla(self):
        """Aplica el gasto en la planilla"""
        print('Aplicando gasto en planilla...')
    

tipo_de_gasto = 'Tarjeta de crédito'
fecha = date(2023, 3, 9)
total = 1320

tarjeta_mc = Gasto( tipo_de_gasto, fecha, total )


tarjeta_mc.show()

tarjeta_mc.total = 1450

tarjeta_mc.show()

tarjeta_mc.aplicar_gasto_en_planilla()

