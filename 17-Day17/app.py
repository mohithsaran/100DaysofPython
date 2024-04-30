# prints each alphabet in the name
name='Mohith'
for i in name:
  print(i)
  if(i=='h'):
    print('This is alphabet h')

#prints all the colors in the list with alphabets
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
    for i in x:
      print(i)

for k in range(1,200):
  print(k)

#prints odd with start value 1 end value 200 step value 2
for k in range(1,201,2):
  print(k)