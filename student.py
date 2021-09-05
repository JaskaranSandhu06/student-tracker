class Student:
    name = ""
    age = 0
    gpa = 0.0
    height = 0.0

    def __init__(self, line):
        a = line.split(",")
        self.name = a[0]
        self.age = int(a[1])
        self.gpa = float(a[2])
        self.height = float(a[3])

    def __str__(self):
        return self.name + "," + str(self.age) + "," + str(self.gpa) + "," + str(self.height)