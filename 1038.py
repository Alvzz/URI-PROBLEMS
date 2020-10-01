x = input().split()
l = int(x[0])
q = int(x[1])
if l == 1:
  total = 4.00 * q
elif l == 2:
  total = 4.50 * q
elif l == 3:
  total = 5.00 * q
elif l == 4:
  total = 2.00 * q
elif l == 5:
  total = 1.50 * q
print('Total: R$ {:.2f}'.format(total))
