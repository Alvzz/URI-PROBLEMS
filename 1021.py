v = float(input())

n100 = v // 100
v = v - n100*100

n50 = v // 50
v = v - n50*50

n20 = v // 20
v = v - n20*20

n10 = v // 10
v = v - n10*10

n5 = v // 5
v = v - n5*5

n2 = v // 2
v = v - n2*2

m1 = v // 1
v = v - m1*1
n1 = float("{:.2f}".format(m1))
v = float("{:.2F}".format(v))

m50 = v // 0.5
v = v - m50*0.5
m50 = float("{:.2f}".format(m50))
v = float("{:.2f}".format(v))

m25 = v // 0.25
v = v - m25*0.25
m25 = float("{:.2f}".format(m25))
v = float("{:.2f}".format(v))

m10 = v // 0.10
v = v - m10*0.10
m10 = float("{:.2f}".format(m10))
v = float("{:.2f}".format(v))

m5 = v // 0.05
v = v - m5*0.05
m5 = float("{:.2f}".format(m5))
v = float("{:.2f}".format(v))

m01 = v * 100
m01 = float("{:.2f}".format(m01))
v = float("{:.2f}".format(v))

print('NOTAS:')
print('{} nota(s) de R$ 100.00'.format(int(n100)))
print('{} nota(s) de R$ 50.00'.format(int(n50)))
print('{} nota(s) de R$ 20.00'.format(int(n20)))
print('{} nota(s) de R$ 10.00'.format(int(n10)))
print('{} nota(s) de R$ 5.00'.format(int(n5)))
print('{} nota(s) de R$ 2.00'.format(int(n2)))
print('MOEDAS:')
print('{} moeda(s) de R$ 1.00'.format(int(m1)))
print('{} moeda(s) de R$ 0.50'.format(int(m50)))
print('{} moeda(s) de R$ 0.25'.format(int(m25)))
print('{} moeda(s) de R$ 0.10'.format(int(m10)))
print('{} moeda(s) de R$ 0.05'.format(int(m5)))
print('{} moeda(s) de R$ 0.01'.format(int(m01)))
