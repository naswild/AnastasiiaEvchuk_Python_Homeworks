class Address:
    def __init__(self, _postcode: str, _city: str, _street: str, _house_number: int, apartment_number: int):
        self.postcode = _postcode
        self.city = _city
        self.street = _street
        self.house_number = _house_number
        self.apartment_number = apartment_number

    def __str__(self):
        return f'{self.postcode}, {self.city}, {self.street}, {self.house_number} - {self.apartment_number}'