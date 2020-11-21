a = input().split()
b = input().split()
c = a + [0] + b
for i in range(len(c)):
    c[i] = int(c[i])
print(c)
good = []
for j in range(len(c)):
    if c[j] >= 90:
        good.append(c[j])
print(good)