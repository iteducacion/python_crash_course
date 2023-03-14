




class Bills():

    def __init__(self, type, date, total):
        self.type = type
        self.date = date
        self.total = total

    def __str__(self):
        print('Vamos a mostrar directamente en pantalla')
        return f"Tipo: {self.type} - Fecha: {self.date} - Total: {self.total}"
        

    def show(self):
        print(f"Tipo: {self.type} - Fecha: {self.date} - Total: {self.total}")