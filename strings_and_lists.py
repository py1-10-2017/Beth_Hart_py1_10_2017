words = "It's thanksgiving day. It's my birthday,too!"

index = words.find("day")
print index
new_str = words.replace("day", "month")
print new_str

x = [2,54,-2,7,12,98]
def newList(list):
    print min(list)
    print max(list)
newList(x);

def firstAndLast(list):
    newList = []
    newList.append(list[0])
    newList.append(list[-1])
    print newList
firstAndLast(x);

y = [19,2,54,-2,7,12,98,32,10,-3,6]
y.sort()
first = y[:5]
second = y[4:]
print second
print first
second.insert(0, first)
print second


#sorts in place; if not sorting in place would save to a var
y.sort() 
first = y[:len(y)/2]
second = y[len(y)/2:]
print first
print second
second.insert(0, first)
print second

#insert does not work when saving to a var -- not sure why
y = [19,2,54,-2,7,12,98,32,10,-3,6]
y.sort()
first = y[:5]
second = y[5:]
print second
newNested =second.insert(0, first)
print newNested