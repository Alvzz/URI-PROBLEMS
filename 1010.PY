linha1 = input().split(" ")
linha2 = input().split(" ")

a1, b1, c1 = linha1
a2, b2, c2 = linha2

total = (int(b1) * float(c1)) + (int(b2) * float(c2))

print("VALOR A PAGAR: R$ {:.2f}".format(total))
