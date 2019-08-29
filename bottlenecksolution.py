x = int(input())
l = list(map(int, input().split()))
m = []
for i in l:
    c = l.count(i)
    m.append(c)
m.sort()
print(m[-1])

