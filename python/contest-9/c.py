import sys
from bisect import bisect
import datetime

def get_datetime(date):
    return datetime.date(*reversed(list(map(int, date.split("-")))))

class Vacations:
    def __init__(self):
        self.changes = [(get_datetime("01-01-0001"), 0)]

    def update_salary(self, date, salary):
        self.changes.append((get_datetime(date), salary))
        self.changes.sort()

    def __call__(self, start, end):
        items = [item[0] for item in self.changes]
        date_end = get_datetime(start)
        date_start = date_end - datetime.timedelta(days=366)
        index_start = bisect(items, date_start)
        index_end = bisect(items, date_end)
        self.clone = self.changes[:]
        self.clone.insert(index_end - 1, (date_end - datetime.timedelta(days=1), self.changes[index_end - 1][1]))
        self.clone.insert(index_start, (date_start, self.changes[index_start - 1][1]))
        #print(self.clone)
        
        temp = self.clone[index_start:index_end + 1]
        #print(temp)

        average = 0
        for di in range(len(temp) - 1):
            average += (temp[di + 1][0] - temp[di][0]).days * temp[di][1]

        average //= 365

        return average * ((get_datetime(end) - date_end).days + 1)
        
my_vacations = Vacations()
my_vacations.update_salary('01-01-2021', 10000)
vacation_salary = my_vacations('01-01-2021', '01-02-2021')
print(vacation_salary)

my_vacations = Vacations()
my_vacations.update_salary('01-01-2021', 100)
my_vacations.update_salary('01-06-2021', 500)
my_vacations.update_salary('01-01-2020', 5000)
vacation_salary = my_vacations('01-01-2021', '01-02-2021')
print(vacation_salary)
