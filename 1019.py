n = int(input())

horas = n // 3600
restoh = n % 3600

minutos = restoh // 60
restom = restoh % 60

segundos = restom

print("{}:{}:{}".format(horas, minutos, segundos))
