x = int(input())
y = str(x)
v = len(y)
mid = v // 2
e = "".join(reversed(y[0:mid + 1]))
if v % 2 == 0 and y[0:mid + 1] == "".join(reversed(y[mid - 1:v])):
    print(1)
elif v == 2 and y[0] == y[1]:
    print(1)
elif y[0] == '-':
    print(0)
elif e == y[mid:v]:
    print(1)
else:
    print(0)
