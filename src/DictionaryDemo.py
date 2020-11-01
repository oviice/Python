Employee = {}
print(type(Employee))
print("printing Employee data .... ")

Employee["Name"] = input("Name: ")
Employee["Age"] = int(input("Age: "))
Employee["Salary"] = float(input("Salary: "))
print("Name : ", Employee["Name"])
print("Age : %d" % Employee["Age"], "Years")
print("Salary : ", Employee["Salary"])
