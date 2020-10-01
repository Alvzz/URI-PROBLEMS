x = float(input())

if (0.00 <= x) and (x <= 2000.00):
    print("Isento")
elif (2000.01 <= x) and (x <= 3000.00):
    t = x - 2000
    tx = t * 0.08
    print("R$ {:.2f}".format(tx))
elif (3000.01 <= x) and (x <= 4500.00):
    t = x - 2000
    ex = t - 1000
    tx1 = 1000 * 0.08
    tx2 = ex * 0.18
    tt = tx1 + tx2
    print("R$ {:.2f}".format(tt))
else:
      t = x - 2000
      ex = t - 1000
      tx1 = 1000 * 0.08
      tx2 = 1500 * 0.18
      ex2 = ex - 1500
      tx3 = ex2 * 0.28
      tt = tx1 + tx2 + tx3
      print("R$ {:.2f}".format(tt))   
