i = 1
j = 7 

while (i < 10):
    for a in range(3):
        print("I={} J={}".format(i, j))
        j += -1 
    i += 2
    j = i + 5
