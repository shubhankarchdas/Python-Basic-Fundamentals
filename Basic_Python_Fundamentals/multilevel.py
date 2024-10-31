class Employee:
    a = 1
class Programmer(Employee):
    b = 2
class Manager(Programmer):
    c = 3

o = Manager()
# print(o.a,o.b,o.c) 
print(f"a is {o.a}\nb is {o.b}\nc is {o.c}")   