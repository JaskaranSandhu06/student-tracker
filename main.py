from student import Student

print("Hello, world!")

students = []


def cmd_create():
    global students
    s = Student("noname,0,0,0")
    s.name = input("Enter the student's name: ")
    s.age = int(input("Enter the student's age: "))
    s.gpa = float(input("Enter the student's GPA: "))
    s.height = float(input("Enter the student's height: "))
    print(s)

def cmd_load():
    global students
    fname = input("Enter the file to load")
    f = open(fname,"r")
    num_loaded = 0
    for line in f:
        s = Student(line)
        students.append(s)
        num_loaded +=1
    print("Loaded "+str(num_loaded)+" students")

while True:
   print(str(len(students))+" students")
   cmd = input("->")
   if cmd == "ping":
       print("Pong!")
   elif cmd == "create":
       cmd_create()
   elif cmd == "load":
       cmd_load()
   elif cmd == "exit":
       print("Goodbye!")
       break
   else:
       print("Command not recognized!")