'''Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A'''
import random
def final_grade(num):
    grade = ""
    for i in range(num):
        score = random.randint(60,100)
        if score >= 60 and score < 70:
            grade = "D"    
        elif score >= 70 and score < 80:
            grade = "C"    
        elif score >= 80 and score < 90:
            grade = "B"   
        elif score >= 90:
            grade = "A"
        print grade
        print "Score: "+ str(score) + "; Your grade is " + grade

final_grade(10)
