names = ['wangfan','wagfan1','wangfan2']

for name in names:
    print(name)

for value in range(1,5):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_number = list(range(2,11,2))
print(even_number)

squers = []
for value in range(1,11):
    squers.append(value ** 2)
print(squers)

print(min(squers))
print(max(squers))
print(sum(squers))