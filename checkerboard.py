# Write a program that prints a 'checkerboard' 
# pattern to the console.

# Your program should require no input and 
# produce console output that looks like 

"""solution 1"""
row = "* "*4
count = 0
while count < 8 :
    if count % 2 == 1:
        print " " + row
    else:
        print row
    count += 1

"""solution 2"""      
row1 = "* "*4
count = 0
while count < 4:
    print row1+ "\n " + row1
    count += 1
    