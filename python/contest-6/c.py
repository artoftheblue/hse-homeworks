import re

def convert_date(date):
    return "-".join(date.split("-")[::-1])

print(convert_date("2026-01-02"))
