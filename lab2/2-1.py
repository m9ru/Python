import random
my_number = random.randint(1,100)
user_number = 101
while my_number <= user_number:
    user_number = int(input('Input number: '))
print('Random number is ' + str(my_number))