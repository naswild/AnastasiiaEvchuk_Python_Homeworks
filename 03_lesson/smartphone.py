class Smartphone:
    def __init__(self, _brand, _model, _subscriber_number):
        self.brand = _brand
        self.model = _model
        self.subscriber_number = _subscriber_number

    def __str__(self):
        return f'{self.brand} - {self.model}. {self.subscriber_number}'