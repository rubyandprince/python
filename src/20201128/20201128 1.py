a = input().split()
b = input().split()
c = a + [0] + b
d = []
for i in range(len(c)):
    c[i] = int(c[i])
print(c)
for j in range(len(c)):
    if c[j] >= 90:
        e = j + 1
        d += [e]
print(d)