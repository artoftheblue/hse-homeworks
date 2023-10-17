def testing(a, b):
    try:
        return int(a) // int(b)
    except ValueError:
        return "Error: ValueError"
    except ZeroDivisionError:
        return "Error: ZeroDivisionError"

print(testing(*input().split()))

