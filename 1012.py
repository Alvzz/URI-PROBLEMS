A = input().split(" ")
a = float(A[0])
b = float(A[1])
c = float(A[2])
q1 = (a * c) * (1/2)
q2 = 3.14159 * c ** 2
q3 = (a + b) * c * (1/2)
q4 = b * b
q5 = a * b
print("TRIANGULO: {:.3f}".format(q1))
print("CIRCULO: {:.3f}".format(q2))
print("TRAPEZIO: {:.3f}".format(q3))
print("QUADRADO: {:.3f}".format(q4))
print("RETANGULO: {:.3f}".format(q5))
