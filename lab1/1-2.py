l = list('list12')
print(l)
print('Even list items:')
for i in range(0,len(l)):
    if i % 2 != 0:
        print(l[i])