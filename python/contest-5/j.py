import sys

class Student:
    HW = "hw"
    TEST = "test"
    EXAM = "exam"
    
    kinds = [HW, TEST, EXAM]
    
    def __init__(self, email, full_name):
        self.email = email
        self.full_name = full_name
        
        self.marks = {
            Student.HW: [],
            Student.TEST: [],
            Student.EXAM: []
        }
        
        self.counts = {
            Student.HW: 0,
            Student.TEST: 0,
            Student.EXAM: 0
        }
        
        self.sums = {
            Student.HW: 0,
            Student.TEST: 0,
            Student.EXAM: 0
        }

    def put_mark(self, mark, kind=HW):
        if kind not in Student.kinds:
            raise TypeError

        if kind == Student.EXAM and self.counts[Student.EXAM] == 1:
            raise IndexError
        
        self.marks[kind].append(mark)
        self.counts[kind] += 1
        self.sums[kind] += mark
        
    def change_mark(self, num, mark, kind=HW):
        if kind not in Student.kinds:
            raise TypeError

        self.sums[kind] -= self.marks[kind][num]
        self.sums[kind] += mark
        self.marks[kind][num] = mark

    def get_result(self, ndigits=2):
        if self.counts[Student.HW] == 0:
            temp1 = 0
        else:
            temp1 = 0.3 * self.sums[Student.HW] / self.counts[Student.HW]
        if self.counts[Student.TEST] == 0:
            temp2 = 0
        else:
            temp2 = 0.3 * self.sums[Student.TEST] / self.counts[Student.TEST]
        return round(temp1 + temp2 + 0.4 * self.sums[Student.EXAM], ndigits)

    def marks_count(self, kind=HW):
        return self.counts[kind]

    def __len__(self):
        return self.count

    def __str__(self):
        return f"{self.email} {self.full_name}"

exec(sys.stdin.read())
