my_tuple = (1, 2, 3, 4, 5)

my_list = list(my_tuple)

print("Before updation : ",my_tuple)

my_list[2] = 6

my_tuple = tuple(my_list)

print("After updation  : ",my_tuple)

# Nested tupple : 
New_Tuple = (1, 54, 45, 5752)  # New Tuple
List = [New_Tuple, 5534, 5643, 98746]  # Creating a nested tuple in list
print("nested tuple in list:", List)  # printing tuple in list