class User:
    def __init__(self, _first_name, _last_name):
        self.first_name = _first_name
        self.last_name = _last_name

    def print_first_name(self):
        print(self.first_name)
        return self.first_name

    def print_last_name(self):
        print(self.last_name)
        return self.last_name

    def print_full_name(self):
        print(f'{self.first_name} {self.last_name}')