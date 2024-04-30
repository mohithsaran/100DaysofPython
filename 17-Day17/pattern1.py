# pattern1
#Print "* * * *" for n=4

# n=int(input('Enter the number to print no of stars: '))
#
# for i in range(n):
#     print('*',end=" ")

#pattern 2
#print square pattern with *
#* * * *
#* * * *
#* * * *
#* * * *
# n=int(input('Enter the number of "*" on a side of square:  '))
# for i in range(n):
#     print('*',end=" ")
#     for j in range(n-1):
#         print('*',end=' ')
#     print()

#print square of 5's
# 5 5 5
# 5 5 5
# 5 5 5
# n=int(input())
# for i in range(n):
#     print('5 '*n)
# print()


#print square of n ex: n=4
#4 4 4 4
#4 4 4 4
#4 4 4 4
#4 4 4 4
# n=int(input())
# # for i in range(n):  #correct
# #     print((str(n)+' ')*n)
#
# for i in range(n): #correct
#     print(n,end=" ")
#     for j in range(n-1):
#         print(n,end=" ")
#     print()


# print pattern
# 1 1 1
# 2 2 2
# 3 3 3
# or
# n=int(input())
# # for i in range(n):
# #     print((str(i+1)+' ')*n)
# for i in range(n):
#     for j in range(n):
#         print(j+1,end=' ')
#     print()


# A A A
# A A A
# A A A
# n=int(input())
# for i in range(n):
#     print('A',end=" ")
#     for j in range(n-1):
#         print('A',end=" ")
#     print()


# A
# B B
# C C C

# n=int(input())
# for i in range(n):
#     print(chr(i+65),end=" ")
#     for j in range(i):
#         print(chr(i+65),end=" ")
#     print()


# * * *
# * *
# *
# n=int(input())
# for i in range(n,0,-1):
#     print('* '*i)
# or
# for i in range(n,0,-1):
#     for j in range(i):
#         print('*', end=" ")
#     print()
# or
# for i in range(n):
#     print('* '*(n-i))


# 1
# 1 2
# 1 2 3
# n=int(input())
# for i in range(n):
#     for j in range(i):
#         print(j+1,end=" ")
#     print()















