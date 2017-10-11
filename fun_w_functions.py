#Create a function called odd_even that counts from 1 
# to 2000. As your loop executes have your program print 
# the number of that iteration and specify whether it's 
# an odd or even number.
# def odd_even(min, max):
#     iteration = 1
#     for i in range (min, max+1):
#         if i %2 ==0:
#             num = "even"
#         else:
#             num = "odd"
#         print "Number is " + str(iteration) + ". The number is " + num + "."
#         iteration += 1
# odd_even(1, 2000)

"""Create a function called 'multiply' that iterates through each
value in a list (e.g. a = [2, 4, 10, 16]) and returns a list 
where each value has been multiplied by 5.
The function should multiply each value in the list by the 
second argument."""

def multiply (list, multiple):
    multiplied = []
    for i in list:
        multiplied.append(i*multiple)
    return multiplied

a = [2, 4, 5]
print multiply(a, 2)

'''Write a function that takes the multiply function call as an
argument. Your new function should return the multiplied list as
a two-dimensional list. Each internal list should contain the 1's
times the number in the original list.'''

def layered_multiples(list, multiple):
    layered_list = []
    for i in list:
        inner_list = []
        for j in range(i*multiple):
            inner_list.append(1)
        layered_list.append(inner_list)
    return layered_list
    
print layered_multiples(multiply(a,2),3)
        
