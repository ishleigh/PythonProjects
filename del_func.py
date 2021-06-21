my_list = [10, 8, 6, 4, 2]
del my_list[1:3] #selecting start and end indexex for deleting
print(my_list)
del my_list[2]# del 1 element
print(my_list)

del my_list[:]#deleting the contents of the list
print(my_list)

my_list = [10, 8, 6, 4, 2]
del my_list # deleting the list itself
#print(my_list) this will cause a runtime error
