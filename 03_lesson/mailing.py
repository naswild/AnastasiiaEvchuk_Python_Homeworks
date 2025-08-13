from address import Address

class Mailing:
    def __init__(self, _to_address: Address, _from_address: Address, _cost: int, _track: str):
        self.to_address = _to_address
        self.from_address = _from_address
        self.cost = _cost
        self.track = _track

    def __str__(self):
        return f'Отправление {self.track} из {self.from_address} в {self.to_address}. Стоимость {self.cost} рублей.'