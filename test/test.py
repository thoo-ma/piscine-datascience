a = list(line for line in open('test.csv'))
b = set(line for line in open('test.csv'))

print(len(a))
print(len(b))

c = list(set([x for x in a if a.count(x) > 1]))
c.sort()

for i in c:
  print(i)