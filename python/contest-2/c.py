string = input()
if "f" in string:
    if "f" in string.replace("f", "", 1):
        print(string.index("f"), len(string) - string[::-1].index("f") - 1)
    else:
        print(string.index("f"))
