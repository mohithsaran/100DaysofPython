l = [3, 5, 6, "String", True]
print(l)
print(type(l))
print(l[0])  #Accessing the list
print(l[3])
print(l[4])

print(l[-2])  # negative index
print(l[len(l) - 2])  #positive index for the above negative index

if 4 in l:  #else is executed
    print("6 is present")
else:
    print('Not present')

color = 'Green'
colors = ["Red", "Green", "Blue", "Yellow", "Green"]
if color in colors:
    print("Green is present.")
else:
    print("Orange is absent.")

#Same applies to strings as well
if "ar" in "Saran":
    print('Yes')

marks = [10, 10, 9, 8, 6, 7, 5, 7]
print(marks)
print(marks[0:])  #index starts from 0 to end
print(marks[-4:])  #index starts from 2 to end
print(marks[1:-1])  # index from 1 to -2 as -1 is not included
print(marks[1:4:2])  #jumps to index by 2 starting from 1 to 4 but 4 not included
print('jumping index by 2 which prints alternative values')
print(marks[1::2])  # jumps to index by 2 starting from 1 to end
print('jumping index by 3')
print(marks[1::3])

#List comprehension
lst = [i for i in range(4)]
print(lst)  #0,1,2,3
lst = [i * i for i in range(10)]
print(lst)  #0,1,4,9,16,....,81
lst = [i * i for i in range(10) if i % 2 == 0]
print(lst)  #[0, 4, 16, 36, 64]
