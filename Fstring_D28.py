#Day 28 of 100

#F string in python

letter = "hey my name is {1} and i am from {0}"
country = "India"
name = "John"

print(letter.format(country, name))
print(f"hey my name is {name} and i am from {country}")
print(f"We have used F string like this : hey my name is {{name}} and i am from {{country}}")