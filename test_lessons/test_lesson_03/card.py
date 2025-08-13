class Card:
    number = '0000 0000 0000 0000'
    valid_date = '01/99'
    holder = 'unknown'

    def __init__(self, number, valid_date, holder):
        self.holder = holder
        self.number = number
        self.valid_date = valid_date

    def pay(self, amount):
        print(f'С карты {self.number} списали {amount}')