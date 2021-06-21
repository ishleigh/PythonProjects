#A slice is an element of Python syntax that allows you 
#to make a brand new copy of a list, or parts of a list.
# Copying the entire list.
list_1 = [1,2,'i']
list_2 = list_1[:]#list_2 takes the values in list_1
list_1[0] = 2 #replacing a value
print(list_2)
print(list_1)

# Copying some part of the list.
my_list = [10, 8, 6, 4, 2]
new_list = my_list[1:3]#The new_list list will have end - start (3 - 1 = 2) 
#elements - the ones with indices equal to 1 and 2 (but not 3)
print(new_list) #8,6
new_list = my_list[1:-1] #negative indexing
print(new_list)
