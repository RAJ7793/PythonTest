
numbers = {
        1:"Ramesh",
        2:"Sunil",
        3:"Santosh"
        }

print(1 in numbers)
print(2 in numbers)
print(3 in numbers)
print(4 in numbers)

print(numbers.get(1))
print(numbers.get(5, "Value is not avilable"))
print(numbers.keys())
print(numbers.values())
print(numbers.items())
print([x,y for x,y numbers.items())

