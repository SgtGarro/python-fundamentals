# CRUD Create, Read, Update, Delete

numbers = [1, 2, 3, 4, 5]
print(numbers[1])

numbers[-1] = 10  # The last position changes the value
print(numbers)

numbers.append(700)  # Insert a new value to the list at the end
print(numbers)

numbers.insert(1, 900)
print(numbers)

tasks = ['to do 1', 'to do 2', 'to do 3']
newList = numbers + tasks
print(newList)

index = newList.index('to do 2')
newList[index] = 'to do changed'
print(newList)

newList.remove('to do 1')
print(newList)

newList.pop()
print(newList)

newList.pop(0)
print(newList)

newList.reverse()
print(newList)

numbersA = [1, 4, 5, 2]
numbersA.sort()
print(numbersA)

strings = ['re', 'ab', 'ed']
strings.sort()
print(strings)
