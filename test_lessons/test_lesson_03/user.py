class User:
    age = 0

    def __init__(self, name): # конструктор
        print('Я создался')
        self.user_name = name # поле user_name

    def say_name(self): # метод
        print('Меня зовут', self.user_name)

    def say_age(self):
        print(self.age)

    def set_age(self, new_age):
        self.age = new_age