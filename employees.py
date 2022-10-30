class employee:
    def __init__(self, name, surname, age, occupation):
        self.name = name
        self.surname = surname
        self.age = age
        self.occupation = occupation
        self.output = ""

    def getname(self):
        self.name = input("What is your name?\n")

    def getsurname(self):
        self.surname = input("What is your surname?\n")

    def getage(self):
        self.age = input("""When were you born? 
DD/MM/YYYY\n""")
        
    def getoccupation(self):
        self.occupation = input("State your occupation.\n")
    
    def getoutput(self):
        output = self.name+","+self.surname+","+str(self.age)+","+self.occupation
        return output

    def save(self):
        employee_file = open("C:\Users\User\Documents\Software Engineering\Projects\Python\JRS", "a")
        employee_file.write(self.getoutput() +"\n")
        employee_file.close()
  
    def getalldetails(self):
        self.getname()
        self.getsurname()
        self.getage()
        self.getoccupation()
        self.getoutput()
        self.save()