countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item
temp.pop(3)                 #remove item
temp[3]="FInland"
print(temp)                  #Prints list
countries=tuple(temp)        #Converted to tuple
print(countries)

southEastAsia=("Indonesia","Singapore","Vietnam")
countries2=countries+southEastAsia
print(countries2)

#tuple methods
tuple1=('0','1','2','2','3','3','4')
res=tuple1.count('2')
print(res)
res=len(tuple1)
print(res)
indexing=tuple1.index('3',3,7)
print(indexing)
indexing=tuple1.index('4',3,7)
print(indexing) #not in tuple slice


