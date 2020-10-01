x = float(input())

if x <= 400.00:
    rg = x * 0.15
    ns = x + rg
    p = 15
elif (400.01 <= x) and (x <= 800.00):
    rg = x * 0.12
    ns = x + rg
    p = 12
elif (800.01 <= x) and (x <= 1200.00):
    rg = x * 0.10
    ns = x + rg
    p = 10
elif (1200.01 <= x) and (x <= 2000.00):
    rg = x * 0.07
    ns = x + rg
    p = 7
else:
    rg = x * 0.04
    ns = x + rg
    p = 4                 
print("Novo salario: {:.2f}".format(ns))
print("Reajuste ganho: {:.2f}".format(rg))
print("Em percentual: {} %".format(p))
    