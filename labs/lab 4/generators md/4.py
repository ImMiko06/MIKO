def squares(a, b):
    result = []
    for i in range(a, b + 1):
        result.append(i ** 2)
    return result

a, b = map(int, input("Enter a and b: ").split())

for num in squares(a, b):
    print(num, end=" ")