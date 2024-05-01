# def avg(a=9,b=1): #default args
#   print("the average is ",(a+b)/2)

# avg(4,5)

# def avg1(a,b,c=2):
#   print("the avg is",(a+b+c)/3)


# avg1(b=1) #since a is not passed it gives error
# avg1(10,3)  #a=10,b=3,c=2 avg is 5

# def avgn(*num):
#   sum=0
#   for i in num:
#     sum+=i
#   print(sum/len(num))

# avgn(10,20,30,40)

# def name(**name):
#     print("Hello,", name["fname"], name["mname"], name["lname"])

# name(mname = "Buchanan", lname = "Barnes", fname = "James")