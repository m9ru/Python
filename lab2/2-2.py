l = ['Hello, Bob', 'Goodbye Mrs. Smith', 'tree', 'grass', 'I\'m going to school', 'cloud']
print('Lines from 5 to 10 characters: ')
for i in l:
    if len(i)>=5 and len(i)<=10:
        print(i + ' -> ' + str(len(i)))