def f():
    a = int(input())
    result = ""
    
    if a != 0:
        result = f()
        
    if a ** 0.5 - int(a ** 0.5) == 0.0 and a != 0:
        return result + " " + str(a)
    return result

x = f()
if x == "":
    x = "0"
print(x)
