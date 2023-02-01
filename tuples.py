numbers = (1, 2, 3, 5)
strings = ("Marce", "Sebas", "Jonas", "Sebas")
print(numbers)
print('0 =>', numbers[0])
print(type(numbers))

print(strings)
print(type(strings))

print(strings.index('Marce'))
print(strings.count('Sebas'))

myList = list(strings)

print(myList)
print(type(myList))

myList[2] = "Johnatan"
print(myList)

myTuple = tuple(myList)
print(myTuple)
print(type(myTuple))
