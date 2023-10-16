import re

def prep_ip(ip):
    return ".".join(str(int(i)) for i in ip.split("."))

print(prep_ip("100101.00001"))
