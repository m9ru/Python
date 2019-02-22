s = 'alkd0sjfl4935kj43jIda'
print('String: ' + s)
sm = ''
for i in s:
    if ord(i) >= 48 and ord(i) <= 57:
        sm += i
print('String containing only numbers: ' + sm)