def create_multi_table(low, high):
    print "%3s" % "x", #uses min 3 spaces in % placeholder, then subs value after % into string
    for i in range(low,high+1):
        print "%3s" % i,
    count = low
    
    while count < (high + low):
        print "\n%3s" % str(count),
        for i in range(low,high+1):
            print "%3s" % str(count*i),
        count += 1
 
create_multi_table(1,12) 
    
