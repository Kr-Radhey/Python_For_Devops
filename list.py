#printing reverse using negative index traversing

list1= [2,3,4,5,6]
i=-1
for li in list1 :
        print(list1[i])
        i = i-1



#slicing
    
new_list = ["this", "is", "list", "for", "slicing"]
print(new_list[1:3])
print(new_list[3:])

#Appending items to list

list1.append(7)
new_list.append("appending this string")
print("List after appending : ", list1)
print("New List after append : ", new_list)

#Extending list

extend = [8,9,10]
list1.extend(extend)
                                            # list2 = list1 + extend   #We can extend with concatenation also.
print("list after extension : ", list1)

#Insertion using Insert()

list1.insert(4, "Inserted Item")
new_list.insert(5, "Inserted Value")
print(f"List1 after insertion : ", list1)
print(f"New_list after insertion : {new_list}")

#Deletion of item from list

list1.remove(4)
print(list1)
new_list.remove("is")
print(new_list)