def func(a,b,c,k):
    try:
        answ = abs((pow(a,2)/pow(b,2)+pow(c,2)*pow(a,2))/(a+b+c*(k-a/pow(b,3)))+c+(k/b-k/a)*c)
    except ZeroDivisionError:
        answ = ('Zero Division Error')
    return answ
a,b,c,k = map(int, input('Input a,b,c,k: ').split())
ans = func(a,b,c,k)
print ('Answer: ' + str(ans))