name = "Marcelo"
print(name)

lastName = "Garro"

fullName = name + " " + lastName
print(fullName)

quote = "I'm Marcelo"
print(quote)

quote2 = 'She said "Hello"'
print(quote2)

# format
template = "Hello, my name is " + name + " and my last name is " + lastName
print(template)

template = "Hello, my name is {} and my last name is {}".format(name, lastName)
print(template)

template = f"Hello, my name is {name} and my last name is {lastName}"
print(template)

age = 19
template = f"Hello, my name is {fullName} and my age is {age}"
print(template)
