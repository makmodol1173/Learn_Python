numbers = [45, 87, 96, 65, 43, 90, 85, 14, 26, 61, 70]
odds=[]
for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)

print(odds)
# odd_nums = [num for num in numbers if num % 2 == 1]
odd_nums = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
print(odd_nums)

names = ['Shah', 'Moaz', 'Rabbi']
ages = [38, 37, 32]

age_comb = []
for name in names:
    print('name:', name)
    for age in ages:
        print(name, age)
        age_comb.append([name, age])
print(age_comb)

age_comb2 = [[name, age] for name in names for age in ages]

print(age_comb2)