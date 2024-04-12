#Create an empty list called my_list.
#Append the following elements to my_list: 10, 20, 30, 40.
#Insert the value 15 at the second position in the list.
#Extend my_list with another list: [50, 60, 70].
#Remove the last element from my_list.
#Sort my_list in ascending order.
#Find and print the index of the value 30 in my_list.


my_list = []

my_list.extend([10,20,30,40])

print(my_list)

my_list.insert(2,50)

your_List = [50, 60, 70]

my_list.extend(your_List)

print(my_list)

my_list.pop()

my_list.sort()

index_of_30 = my_list.index(30)

print("Index of 30 in my_list:", index_of_30)

print("my_list:", my_list)
