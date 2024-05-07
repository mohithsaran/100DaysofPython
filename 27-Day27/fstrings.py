letter="Hey my name is {} and Iam from {}"
country="India"
name="Mohith"

print(letter.format(name,country))
#print(letter.format(country,name)) #correct order is required according to the format
 #or
letter="Hey my name is {1} and Iam from {0}"
country="USA"
name="Mohith"
print(letter.format(country,name)) #according to index

print(f"Hey my name is {name} and Iam from {country}")

price=40.01299
txt = f"For only {price:.2f} dollars!"
print(txt)


print(f"{2 * 30}")