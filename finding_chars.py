# Write a program that takes a list of strings 
# and a string containing a single character, and 
# prints a new list of all the strings containing 
# that character.

def find_char_words(char, list): 
    char_words = []
    for word in list:
        if char in word:
            char_words.append(word)
    print char_words
        
        
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
find_char_words(char, word_list)
