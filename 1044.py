x = input().split()
a = int(x[0])
b = int(x[1])
if(a % b == 0) or (b % a == 0):
  print('Sao Multiplos')
else:
  print('Nao sao Multiplos')
