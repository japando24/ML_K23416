class Product:
    def __init__(self,id = None, name = None, price = None, quantity = None):
        self.id=id
        self.name = name
        self.quantity=quantity
        self.price = price
    def __str__(self):
        return f"{self.id} {self.name} {self.quantity} {self.price}"