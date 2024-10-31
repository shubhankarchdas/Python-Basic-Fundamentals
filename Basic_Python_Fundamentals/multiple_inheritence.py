class Employee:
    company = "EXTEN" #base class
    name = "default name"

    def show(self):
        print(f"The name is {self.name} and the company is : {self.company}")
        
class Coder:
    language = "python"
    def printLanguage(self):
        print(f"Outer of all the language here is your language : {self.language}")



class Programmer(Employee,Coder): #derived class
    company = "EXTRN Infotech"
    def showLanguage(self):
        print(f"The name is : {self.company} and he is good with  : {self.language}")

a= Employee()
b=Programmer()

# print(a.company,b.company)

b.show()
b.printLanguage()
b.showLanguage()