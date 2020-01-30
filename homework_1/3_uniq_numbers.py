numbers = [int(i) for i in input().split()]
result = set()

for i in numbers:
    if numbers.count(i) > 1:
        result.add(i)

if len(result) == 0:
    print("All numbers in string are uniq!")
else:
    for r in result:
        print(r, end=" ")
