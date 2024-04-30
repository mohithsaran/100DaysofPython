a=int(input('Enter the base value: '))
b=int(input('Enter the power value: '))
value=1

for i in range(1,b+1):
    value*=a
print(a,' to the power of', b ,' value is ',value)