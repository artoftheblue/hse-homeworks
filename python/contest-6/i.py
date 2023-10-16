from itertools import product

suits = ["пик", "треф", "бубен", "червей"]
values = [char for char in "23456789"] + ["10", "валет", "дама", "король", "туз"]
suit = input()
suits.remove(suit)

for item in product(values, suits):
    print(*item)
