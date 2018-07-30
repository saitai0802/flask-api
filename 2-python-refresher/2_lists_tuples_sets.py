my_variable = 'hello'
my_list_variable = ['hello', 'hi', 'nice to meet you']

 # immutable object, we can't modify after initizalted.
my_tuple_variable = ('hello', 'hi', 'nice to meet you')

# unique and unordered (Python will print out the number randomly, and we can'y user syntax like set_var[0])
my_set_variable = {'hello', 'hi', 'nice to meet you'}

print(my_list_variable[0])
print(my_tuple_variable[0])
print(my_set_variable[0])  # This won't work, because there is no order. Which one is element 0?



# --------------- Expeiriment Test --------------

###### List variable
my_list_variable.append('another string')
print(my_list_variable)

###### Tuple variable
my_tuple_variable.append('a string')  # This won't work, because a tuple is not a list.
my_tuple_variable = my_tuple_variable + ("a string",)
print(my_tuple_variable)
my_tuple_variable[0] = 'can I change this?'  # No, you can't

###### Set variable
my_set_variable.add('I want to add same value')
print("First add:" + my_set_variable)
my_set_variable.add('I want to add same value')
print(my_set_variable)
print("Second add:" + my_set_variable)



# --------------- Operational Test --------------

###### Tuple Operations (Remember we only calulate a new tuple not modify the set_one)
set_one = (5, 7, 9)

# it has to be a comma after the number or else python will think that is a 10 with braket with it!
# orelse it will think it is a mathematical equation.
set_twe = (10,)
print(set_one + set_twe) # ans: 5, 7 ,9 ,10


###### Set Operations
set_one = {1, 2, 3, 4, 5}
set_two = {1, 3, 5, 7, 9, 11}

print(set_one.intersection(set_two))  # {1, 3, 5}
print({1, 2}.union({2, 3}))  # {1, 2, 3}
print({1, 2, 3, 4}.difference({2, 4}))  # {1, 3}
