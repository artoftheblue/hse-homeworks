string = input()
if "f" in string:
    string = string.replace("f", "", 1)
    if "f" in string:
        print(string.index("f") + 1)
    else:
        print(-1)
else:
    print(-2)
