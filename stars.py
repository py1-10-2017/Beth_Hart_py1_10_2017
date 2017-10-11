"""Part I
Create a function called draw_stars() that takes a list of numbers
and prints out *."""

def draw_stars(list):
    for i in list:
        print i*"*"
draw_stars([5,2,3])

"""PART II
Modify the function above. Allow a list containing integers and 
strings to be passed to the draw_stars() function. When a string 
is passed, instead of displaying *, display the first letter of 
the string according to the example below. 
You may use the .lower() string method for this part."""

def draw_stars_letters(list):
    for item in list:
        if isinstance(item, str):
            print str.lower(item[0])*len(item)
        else:
            print item*"*"
            
draw_stars_letters([5, "Beth", 4, "Mikayla"])