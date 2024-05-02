l=[1,2,3]
print(l)
l.append(4)
print(l)
l.append(0)
print(l)
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
l.reverse()
print(l)
print(l.index(3))

# m=l
# m[0]="Mohith"
# print(l)
m=l.copy()
m[0]="Mohith"
print(l)
print("This is m list ",m)

l.insert(3,607)
print(l)

colors=['pink','purple','brown']
rainbow=['Violet','Indigo','Blue','Green','Yellow','Orange','Red']

# colors.extend(rainbow)
# print(colors)

k=colors+rainbow
print(k)