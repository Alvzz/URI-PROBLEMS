linha = input().split()

a, b, c, d = linha

a = int(a)
b = int(b)
c = int(c)
d = int(d)

if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and a % 2 == 0:
  print("Valores Aceitos")
else:
    print("Valores nao aceitos")  
