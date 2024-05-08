def fact(num):
  if(num==1 or num==0):
    return 1
  else:
    return(num*fact(num-1))

n=int(input("Enter a number for factorial: "))
print(f"Factorial of {n}: ",fact(n))