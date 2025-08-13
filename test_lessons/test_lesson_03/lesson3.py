from user import User
from card import Card

alex = User('Alex') #создай мне новый экземпляр класса User
mark = User('Mark') #создай мне новый экземпляр класса User
marta = User('Marta') #создай мне новый экземпляр класса User

alex.say_name()
alex.set_age(33)
alex.say_age()

card = Card('4539 3857 3847 8573', '11/28', 'Alex F')
card.pay(1000)
