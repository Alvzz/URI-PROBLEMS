x = input().split()
i, f = x
i = int(x[0])
f = int(x[1])
if i < f:
    h = f - i
else:
    h = (24 - i) + f
print('O JOGO DUROU {} HORA(S)'.format(h))
