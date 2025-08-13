class Book:
    def __init__(self, _name: str, _autor: str):
        self.name = _name
        self.autor = _autor

    def get_name(self) -> str:
        return self.name
    def get_autor(self) -> str:
        return self.autor