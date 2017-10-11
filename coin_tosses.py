"""Write a function that simulates tossing a coin 5,000 times. 
Your function should print how many times the head/tail appears."""
import random
def coin_toss(tosses):
    heads = 0
    tails = 0
    for toss in range(tosses):
        num = random.random()
        if num < .5:
            heads += 1
            outcome = "heads"
        elif num >= .5:
            tails += 1
            outcome = "tails"
        print "Attempt #:",toss,"You flipped", outcome, "Total heads =",heads, " Total tails: ", tails
        
coin_toss(50)

            
    