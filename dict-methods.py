person = {
    'name': 'Marcelo',
    'lastName': 'Garro',
    'langs': ['javascript', 'c++', 'css', 'html'],
    'age': 19
}

print(person)

# Modify
person['name'] = 'Chelo'
person['age'] -= 1
person['langs'].append('rust')
print(person)

# Delete
del person['lastName']
person.pop('age')
print(person)

print('\nItems')
print(person.items())

print('\nKeys')
print(person.keys())

print('\nValues')
print(person.values())
