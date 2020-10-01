vp = 0 
m = 0 

for _ in range(6):
    n = float(input())
    if n > 0: 
        vp += 1
        m = m + (n)

print("{} valores positivos".format(vp))
print("{:.1f}".format(m/vp))
