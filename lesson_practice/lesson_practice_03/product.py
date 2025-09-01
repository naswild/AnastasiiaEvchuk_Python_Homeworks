class Product:
    def __init__(self, _name: str, _price: int):
        self.name = _name
        self.price = _price

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_info(self):
        return f'Product: {self.name}, price: {self.price}'