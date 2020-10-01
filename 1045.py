x = input().split()

a = float(x[0])
b = float(x[1])
c = float(x[2])

a, b, c = sorted([a, b, c], reverse=True)

if  a >= b + c:
    print("NAO FORMA TRIANGULO")
else:    
    if a ** 2 == b ** 2 + c ** 2:
        print("TRIANGULO RETANGULO")
    if a ** 2 > b ** 2 + c **2: 
        print("TRIANGULO OBTUSANGULO")   
    if a ** 2 < b ** 2 + c ** 2:
        print("TRIANGULO ACUTANGULO") 
    if a == b  and b == c:
        print("TRIANGULO EQUILATERO")  
    elif (a == b and b != c) or (b == c and c != a) or (a == c and b != a):
        print("TRIANGULO ISOSCELES")                 
