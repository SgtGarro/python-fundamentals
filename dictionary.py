myDict = {}
print(myDict)
print(type(myDict))

myDict = {
    'name': "Marcelo",
    'lastName': "Garro",
    'age': 87,
}
print(myDict)
print(len(myDict))

print('Last Name =>', myDict['lastName'])
print(myDict.get('age'))

print(myDict.get('none'))  # If an error occurred, returns "None"
print(myDict['none'])  # If an error ocurred, it crash the program
