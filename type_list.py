# Write a program that takes a list and prints a message 
# for each element in the list, based on that element's data type.

# Your program input will always be a list. For each item in the list, test its data type. If the 
# item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. 
# At the end of your program print the string, the number and an analysis of what the list contains. 
# If it contains only one type, print that type, otherwise, print 'mixed'.

# Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?
one = ['magical unicorns',19,'hello',98.98,'world']
two = [2,3,1,7,4,12]
three = ['magical','unicorns']
def type_list(list):
    string = ""
    sum = 0
    for i in list:
        if isinstance(i,str):
            string = string+ " " + i
        elif isinstance(i,int) or isinstance(i,float):
            sum += i
    print "string: ", string
    print "sum: ", sum
    if sum !=0 and string > 0:
        print "list is a mixed type"
    elif sum > 0 and string == 0:
        print "list is all numbers"
    elif string > 0 and sum == 0:
        print "list is all strings"

type_list(one)
type_list(two)
type_list(three)
