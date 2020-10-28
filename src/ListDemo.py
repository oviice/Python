list1 = [1, 2, 3, 4, 5]
list2 = {1, 4, 3, 5}
for i in list1:
    print(i)
    if i == 4:
        continue
print("End of for loop")
print(type(list1))
