cp = 0
ci = 0
cpi = 0
cn = 0

for _ in range(5):
    n = int(input())
    if n % 2 == 0:
        cp += 1
    else:
        ci += 1
    if n > 0:
        cpi += 1
    if n < 0:
        cn += 1

print("{} valor(es) par(es)".format(cp))
print("{} valor(es) impar(es)".format(ci))
print("{} valor(es) positivo(s)".format(cpi))
print("{} valor(es) negativo(s)".format(cn))
