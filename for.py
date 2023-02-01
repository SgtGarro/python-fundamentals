""" for element in range(20):
    print(element) """

myList = [23, 45, 67, 89, 43]

for i in myList:
    print(i)

myTuple = ('nico', 'july', 'santi')
for i in myTuple:
    print(i)

product = {
    'name': 'T-shirt',
    'price': 100,
    'stock': 89
}
""" for key in product:
    print(key, '=>', product[key])
 """
for key, value in product.items():
    print(key, '=>', value)

people = [
    {
        'name': 'Marcelo',
        'age': 19
    },
    {
        'name': 'Sebas',
        'age': 23
    },
    {
        'name': 'John',
        'age': 27
    }
]

for person in people:
    print('name =>', person['name'])
