an = input().split()
ow = input().split()

print(an, ow)

an = sorted(an)
ow = sorted(ow)

ans = []
for a in an:
    isFound = False
    for o in ow:
        if o[0] == a[0]:
            isFound = True
    if not isFound:
        ans.append(a)

print(*ans, sep=' ')