import re

def check_good_word(text):
    temp = text.replace(" ", "")
    pattern = re.compile(r"^[A-Za-z0-9]+$", re.IGNORECASE)
    if pattern.match(temp):
        return "YES"
    return "NO"

print(check_good_word("JDAJSDJASD JADSJSAD"))
