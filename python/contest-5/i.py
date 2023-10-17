import sys

class Student:
    def __init__(self, email: str, full_name: str):
        self.email = email
        self.full_name = full_name
        self.marks = []
        self.count = 0

    def put_mark(self, mark: int):
        self.marks.append(mark)
        self.count += 1

    def change_mark(self, num: int, new_mark: int):
        self.marks[num] = new_mark

    def get_result(self):
        if self.marks == []:
            return 0
        return round(sum(self.marks) / self.count, 2)

    def __len__(self):
        return self.count

    def __str__(self):
        return f"{self.email} {self.full_name}"

exec(sys.stdin.read())