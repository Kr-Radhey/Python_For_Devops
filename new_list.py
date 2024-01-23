#Deletion using del statement

string = input("Please enter list items: ")
#index = int(input("Please input index number which you want to remove : "))

list1 = string.split()
print("List items before deletion : ", list1)


#del list1[index]
#print("List after deletion : ", list1)

#Deleting blank spaces
'''i=0
for blank in list1 :
    if blank == ' ' :
        del list1[i]                 #del statement
    i += 1'''

print("List after removing blank spaces : ", list1)
