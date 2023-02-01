if True:
    print('Hello world')

if False:
    print("It'll never execute")

pet = input('Which is your favorite pet? ')

if pet == "Dog":
    print("You like dogs. That's awesome")
elif pet == "Cat":
    print("I hope you got luck")


stock = int(input("Digit the stock => "))

if stock >= 100 and stock <= 1000:
    print('Stock is correct')
else:
    print("Stock is incorrect")
