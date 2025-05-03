''' LONGEST WORD PER ROW

Given a list of words, return the longest word that can be typed using only one row of a QWERTY keyboard.

example:
words = ["typewriter", "gas", "dad", "pop", "zoo", "queen"]
'''

def check_row(letter):
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    for row in rows:
        if letter in row:
            return row



words = ["gas", "dad", "pop", "typewriter", "zoo", "queen"]

#"typewriter"

longest_words = []
# store the largest length per word
longest = words[0]



# iterate through the list
for word in words:  
    row = check_row(word[0])    # takes the row of the first letter of the word
    count = 0                   
    
    # counts the number of letters with the same row as the row of the first letter
    for c in word:
        if check_row(c) == row:
            count += 1
        
    # if the length of the word is not equal to the count, there must be atleast one letter that does not belong to the same row
    if count == len(word) and len(word) > len(longest):
        longest = word

print(len(longest))

for word in words:
    if len(word) == len(longest):
        longest_words.append(word)

print(longest_words)



       
                



# use a function that checks if the letter is within the rows


# if yes, check if the length of that word is larger than the largest stored length.





# for c in word:              # for every character, check if same with the row of the first one.
    #     # if one character is not the same, remove the word from the list and move on to the next word
    #     if check_row(c) != row:
    #         word_to_remove = word
    #         continue
    # # remove word
    # if word_to_remove != '':
    #     words.remove(word)
    # print(words)
