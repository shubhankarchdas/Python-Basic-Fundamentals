class Employee:
    language = "python"  
    salary = 10000000000


    def __init__(self,name,salary,language): #dunder method which is aucomatically called
        self.name =name
        self.salary=salary
        self.language=language
        print("i am create an object")

    
    
    def getInfo(self):
        print(f"the language is {self.language}.the salary is {self.salary}")

    def greet(self):
        print("tell what you want?") 

    @staticmethod    #decorator   
    def greet():
        print("tell what you want?")    

shubh = Employee("ssss",1000000,"py")
# shubh.name= "shubhankar"
print(shubh.name,shubh.salary,shubh.language)

# abc=Employee()


