# Magic 8 Ball
# Concepts focused on: Functions

import random

def shake_ball(num) : 
    if num == 0:
        return 'Stop playing here. Do your schoolworks!'
    elif num == 1:
        return 'It is certain'
    elif num == 2:
        return 'It is decidedly so'
    elif num == 3:
        return 'Yes'
    elif num == 4:
        return 'Hazy reply, try again!'
    elif num == 5:
        return 'Ask again later'
    elif num == 6:
        return 'Concentrate and ask again'
    elif num == 7:
        return 'My reply is no'
    elif num == 8:
        return 'Outlook not looking so good'
    elif num == 9:
        return 'Very doubtful'

# List approach
def shake_ball_list(num):
    messages = ['Stop playing here', 
        'It is certain',
        'It is decidedly so',
        'Yes definitely',
        'Reply hazy try again',
        'Ask again later',
        'Concentrate and ask again',
        'My reply is no',
        'Outlook not so good',
        'Very doubtful']
    return messages[num]



print("\nMagic 8 Ball!")



while True:
    question = input("\nAsk your question: ")
    if question == 'stop':
        break

    # get the average of 10 results (for better chance)
    num = random.randint(0,9)

    print(shake_ball_list(num))

    print("\n\tEnter 'stop' to end program.")
    
    

print("\nHope I gave you clarity babes!")

