l = 1
r = 1 
while (l != 0) and (r != 0):
    tl = 0
    tr = 0 
    l,r = map(int, input().split())
    if l != 0 and r != 0:
        tl += l 
        tr += r
        print(tl+tr)
