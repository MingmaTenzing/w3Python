list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

list2.append(3)
print(list2)



x = list1[0]
list1[0] = list1[1]
list1[1]= x
print(list1)