
f = open("file.txt", "r")
#data = f.read()
# print(data)
# f.close()


# data = f.readlines()
# print(data, type(data))

# data1 =f.readline()
# print(data1, type(data1))
# data2 =f.readline()
# print(data2, type(data2))
# data3 =f.readline()
# print(data3, type(data3))
# data4 =f.readline()
# print(data4, type(data4))

# data9 = f.readline()
# print(data9)


line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()
