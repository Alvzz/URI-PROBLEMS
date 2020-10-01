x = map(int,input().split())

A, B, C = x

x = sorted([A, B, C], reverse=False)

print("{}".format(x[0]))
print("{}".format(x[1]))
print("{}".format(x[2]))
print()
print("{}".format(A))
print("{}".format(B))
print("{}".format(C))
