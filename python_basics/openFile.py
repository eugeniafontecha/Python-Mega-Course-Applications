myfile = open("fruits.txt")
print(myfile.read())
myfile.close()

with open("fruits.txt") as myfile:
    content = myfile.read()

print(content)

with open("vegetables.txt", 'w') as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")
    myfile.write("Garlic")

with open("vegetables2.txt", 'w') as myfile:
    myfile.write("Tomato\nCucumber\nOnion\n")

with open("vegetables2.txt", 'a') as myfile:  #a es de append. No sobreescribe
    myfile.write("Garlic\n")

with open("vegetables2.txt", 'a+') as myfile:  #a+ además permite leer. Pero tener en cuenta que lee desde donde quedó el cursor
    myfile.write("Garlic")
    myfile.seek(0) #llevamos el cursor a la posición 0
    content = myfile.read()

print(content)

