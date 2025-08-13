class Student:
    def __init__(self, _first_name: str, _last_name: str, _age: int, _course: str):
        self.first_name = _first_name
        self.last_name = _last_name
        self.age = _age
        self.course = _course

    def __str__(self):
        return (f'first name - {self.first_name}, last name - {self.last_name}, '
                f'age - {self.age}, course - {self.course}')
