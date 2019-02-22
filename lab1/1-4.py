import random
l = []
for i in range(0,random.randint(5,20)):
    l.append(random.randint(-100,100))
print('List: ' + str(l))
print('Max of list: ' + str(max(l)))