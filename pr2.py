class Person:
    def __init__(self, Name, setNumber, setAdress):
        self.Name=Name
        self.setNumber=setNumber
        self.setAdress=setAdress
class Student(Person):
    def __init__(self, Name, setNumber, setAdress, enterDate, status):
         Person.__init__(self, Name, setNumber, setAdress)
        
         self.enterDate=enterDate
         if (status == "freshman" or status =="sophomore"or status =="junior"or status =="senior"):
          self.status=status
class Employee(Person):
    def __init__(self, Name, setNumber, setAdress, tarikhestekhdam, setSalary):
        Person.__init__(self, Name, setNumber, setAdress)
      
        self.tarikhestekhdam= tarikhestekhdam
        self.setSalary=setSalary

Reza=Student("reza", 922387465,"Mashhad", "1402/2/5", "man")
Jack=Employee("jack", 284847538, "Tehran", "1402/5/3", 23490)
print(Reza,Jack)
       