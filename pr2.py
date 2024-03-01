class Person:
    def __init__(self, Name):
      self.Name=Name
   
    def set_setNumber(self,setNumber):
        self.setNumber=setNumber
    def set_setAdress(self,setAdress):
        self.setAdress=setAdress  
    
    def get_printsetnumber(self):
        return self.setNumber
    def get_printsetAdress(self):
        return self.setAdress
   
class Student(Person):
    def __init__(self, Name, setNumber, setAdress):
         Person.__init__(self, Name, setNumber, setAdress)
    
    def set_enterDate(self, enterDate):
        self.enterDate=enterDate    
    def set_status(self,status):
        self.status=status
        
    def get_printstatus(self):
        if self.status=="freshman" or "sophomore"or "junior"or"senior":
            return self.status
        else:
            return "false"
    def get_printStudent(self):
        return self.enterDate, self.status   

class Employee(Person):
    def __init__(self, Name, setNumber, setAdress):
        Person.__init__( self, Name, setNumber, setAdress)
    
    def set_tarikhestekhdam(self, tarikhestekhdam):   
        self.tarikhestekhdam=tarikhestekhdam
    def set_Salary(self, Salary):
        self.Salary=Salary
    
    def get_printEmployee(self):
        return self.tarikhestekhdam, self.Salary

Judie=Student("Judie", 922387465,"Mashhad","1402/2/5", "man")
Jack=Employee("Jack", 284847538, "Tehran", "1402/5/3", 23490)

print(Judie.get_printStudent())
print(Jack.get_printEmployee())
       