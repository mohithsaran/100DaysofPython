# def fibonacci(num):
#     # 0,1,1,2,3,5,8,13
#     if(num<=1):
#         return num
#     else:
#         return fibonacci(num-1)+fibonacci(num-2)
#
# n=int(input("Enter the input:"))
# print("Fibonacci number for the series: ")
# for i in range(n):
#     print(fibonacci(i),end=" ")

a=0
b=1
num=int(input("Enter a number for a range of fibonacci numbers:"))
print(a)
print(b)
for i in range(num-2):
    c=a+b
    a=b
    b=c
    print(c)


