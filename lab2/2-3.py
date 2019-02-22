import random
rus = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
string = ''
print('Random string of 5 characters:')
for i in range(5):
    string += rus[random.randint(0,32)]
print(string)