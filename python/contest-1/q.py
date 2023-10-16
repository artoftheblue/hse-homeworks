numbers = [int(input()), int(input())]
numbers.sort(reverse=True)
a = int(input())
while a != 0:
    if a > numbers[0]:
        numbers[1] = numbers[0]
        numbers[0] = a
    elif a > numbers[1]:
        numbers[1] = a
    a = int(input())
print(numbers[1])
