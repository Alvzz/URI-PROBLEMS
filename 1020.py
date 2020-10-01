id = int(input())

anos = id // 365
restoa = id % 365

meses = restoa // 30
restom = restoa % 30

dias = restom

print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))
