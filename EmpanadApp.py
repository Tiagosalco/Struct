class EmpanadApp:
    
    def __init__(self):
        self.reuniones = []
        
    def crear_reunion(self, gustos_empanadas, precio):
        reunion = {'gustos': gustos_empanadas, 'precio': precio, 'pedidos': {}}
        self.reuniones.append(reunion)
        return len(self.reuniones) - 1
        
    def agregar_pedido(self, reunion_id, usuario, gusto_empanada, cantidad):
        reunion = self.reuniones[reunion_id]
        if gusto_empanada not in reunion['gustos']:
            return False
        if usuario not in reunion['pedidos']:
            reunion['pedidos'][usuario] = {}
        reunion['pedidos'][usuario][gusto_empanada] = cantidad
        return True
        
    def listar_pedidos(self, reunion_id):
        reunion = self.reuniones[reunion_id]
        return reunion['pedidos']
    
    def calcular_total_empanadas(self, reunion_id):
        reunion = self.reuniones[reunion_id]
        total_empanadas = {}
        for gusto in reunion['gustos']:
            cantidad = 0
            for usuario, pedidos in reunion['pedidos'].items():
                if gusto in pedidos:
                    cantidad += pedidos[gusto]
            total_empanadas[gusto] = cantidad
        return total_empanadas