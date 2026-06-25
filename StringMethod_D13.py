#day 13 

#String method 

#1. Upper() method
a = "helllo"
print(a.upper()) #HELLO

#2. Lower() method
print(a.lower()) #hello

#3. rstrip() method
print(a.rstrip("o")) #hell

#4. replace() method
print(a.replace("l", "p")) #heppo

#5. split() method
print(a.split("l")) #['he', '', 'o']

#6. capitalize() method
print(a.capitalize()) #Hello

#7. center() method
print(a.center(20, "*")) #*******hello********

#8. count() method
print(a.count("l")) #2

#9. endwith() method
print(a.endswith("o")) #True

#10. find() method
print(a.find("l")) #2

#11. index() method
print(a.index("l")) #2

#13. isalnum() method  
print(a.isalnum()) #False

#14. isalpha() method
print(a.isalpha()) #False

#15. isdigit() method
print(a.isdigit()) #False

#16. islower() method
print(a.islower()) #True

#17. isupper() method
print(a.isupper()) #False

#18. isprintable() method
print(a.isprintable()) #True

#19. isspace() method
print(a.isspace()) #False

#20. istitle() method
print(a.istitle()) #False

#21. startswith() method
print(a.startswith("h")) #True


