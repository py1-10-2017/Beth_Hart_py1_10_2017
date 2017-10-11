'''Given the following list:'''

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

'''Create a program that outputs:

Michael Jordan
John Rosales
Mark Guillen
KB Tonel'''

def student_roster(list):
    for item in list:
        print item["first_name"] + " " + item["last_name"]
student_roster(students)
            
    


'''Part II
Now, given the following dictionary:'''

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
'''Create a program that prints the following format (including number of characters in each combined name):
Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13'''

def students_formatted(dict):
    num = 1
    for key in dict:
        print key
        for value in dict[key]:
            full_cap_name = str.upper(value["first_name"]+ " " + value["last_name"])
            num_chars = len(value["first_name"] + value["last_name"])
            print str(num) + " - " + full_cap_name + " - " + str(num_chars)
            num += 1

students_formatted(users)