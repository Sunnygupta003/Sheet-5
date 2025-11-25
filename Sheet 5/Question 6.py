a = list(map(int, input().split()))

even = 0
odd = 0

for i in a:
    if i % 2 == 0:
        even = even+1
    else:
        odd = odd+1

if even > odd:
    print(even - odd)
else:
    print(odd - even)
