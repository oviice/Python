fileptr = open("C:\\Users\\Ovi\\Desktop\\main.txt", "r")
content = fileptr.readline()
print(fileptr)
if fileptr:
    print("file is opened successfully")
fileptr.close()
