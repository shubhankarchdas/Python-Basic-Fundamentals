class Employee:
    company = "EXTEN" #base class
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")
        

# class Programmer:
#     company = "EXTRN Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")
# class ShowLanguage:
#     def show(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")



class Programmer(Employee): #derived class
    company = "EXTRN Infotech"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

a= Employee()
b=Programmer()

print(a.company,b.company)