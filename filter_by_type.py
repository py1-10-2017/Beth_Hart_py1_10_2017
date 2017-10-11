# Integer
# If the integer is greater than or equal to 100, print "That's a big number!" If the integer is less than 100, print "That's a small number"

# String
# If the string is greater than or equal to 50 characters print "Long sentence." If the string is shorter than 50 characters print "Short sentence."

# List
# If the length of the list is greater than or equal to 10 print "Big list!" If the list has fewer than 10 values print "Short list."

def filter_type(el):
    if isinstance(el, int):
        print str(el), "is a number"
        if el >= 100:
            print "that's a big number"
        else:
            print "that's a small number"
        
    if isinstance(el, str):
        print str(el), "is a string"
        if len(el) >= 50:
            print "long sentence"
        else:
            print "short sentence"
    if isinstance(el, list):
        print str(el), "is a list"
        if len(el) >= 10:
            print "that's a long list"
        else:
            print "that's a short list"
            
filter_type(45)
filter_type(100)
filter_type(455)
filter_type(0)
filter_type(-23)
filter_type("Rubber baby buggy bumpers")
filter_type("Experience is simply the name we give our mistakes")
filter_type("Tell me and I forget. Teach me and I remember. Involve me and I learn.")
filter_type("")
filter_type([1,7,4,21])
filter_type([3,5,7,34,3,2,113,65,8,89])
filter_type([4,34,22,68,9,13,3,5,7,9,2,12,45,923])
filter_type([])
filter_type(['name','address','phone number','social security number'])