a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = []

for i in a:
    for j in b:
        c.append(i + j)

print(c)
