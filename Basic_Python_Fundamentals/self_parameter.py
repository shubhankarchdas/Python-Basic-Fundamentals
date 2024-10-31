class Employee:
    language = "python"  
    salary = 0.1


    def getInfo(self):
        print(f"the language is {self.language}.the salary is {self.salary}")

    def greet(self):
        print("tell what you want?") 

    @staticmethod    #decorator   
    def greet():
        print("tell what you want?")    

shubh = Employee()
shubh.language= "C++"
# print(shubh.language,shubh.salary) 

shubh.getInfo()
# Employee.getInfo(shubh)
shubh.greet()

