tup=(1,5,6,"green",True)
print(type(tup))
# tup1=(1)
# print(type(tup1))
# tup[0]=90
print(tup[0])
print(tup[1])
print(tup[4])
#negative indexing
print('Negative indexing')
print(tup[-1])
print(tup[-2])

#check for an item
if True in tup:
  print('Yes')
else:
  print('No')

#slicing
print(tup[2:]) #(6, 'green', True)
print(tup[-4:-1]) #except -1 #(5, 6, 'green')
print(tup[1::2]) #jumping by 2 indices #(5, 'green')


