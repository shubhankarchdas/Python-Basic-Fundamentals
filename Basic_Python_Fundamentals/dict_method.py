marks ={
    "abc" : 100,
    "xyz" : 200,
     0 : "abcdef"
}
print(len(marks))
# print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"abc" : 50})
print(marks)
print(marks.get("abc2")) #print none
print(marks["abc2"]) #returns an error