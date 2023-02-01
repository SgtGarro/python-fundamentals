x = 3.3
y = 1.1 + 2.2

print(x)
print(y)

print(x == y)

yStr = format(y, ".2g")
print('str =>', yStr)

print('*' * 10)
print(y, x)

tolerance = 0.00001
print(abs(x - y) < tolerance)

print(round(y, 1))
