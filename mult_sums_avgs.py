
#print odd from 1-1000
for i in range(1, 1001, 2):
    print i
    
#multiples of 5 to 1,000,000
multiple = 1
result = 1
while result < 1000000:
    result = 5*multiple
    multiple += 1
    print result

# sum list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for i in a:
    sum += i
print sum

#print avg
sum = 0
for i in a:
    sum += i
avg = sum/len(a)
print avg
    
    