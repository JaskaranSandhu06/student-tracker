from student import Student

print("Hello, world!")

def cmd_create():
    s = Student("noname,0,0,0")
    s.name = input("Enter the student's name: ")
    s.age = int(input("Enter the student's age: "))
    s.gpa = float(input("Enter the student's GPA: "))
    s.height = float(input("Enter the student's height: "))
    print(s)

while True:
   cmd = input("->")
   if cmd == "ping":
       print("Pong!")
   elif cmd == "create":
       cmd_create()
   else:
       print("Command not recognized!")

