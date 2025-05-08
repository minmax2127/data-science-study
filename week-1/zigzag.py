''' Falling Zigzag
     **********
    **********
   **********
  **********
 **********
**********
 **********
  **********
   **********
    **********
     **********
    **********
   **********
  **********
 **********
**********
 **********
  **********
   **********
    **********
     **********
'''


import time, sys

base_space_count = 5
indent_count = base_space_count
zigzag_width = 10

row = ""
toLeft = True # start direction to the left of the screen

try:
    while True:
        # generates a row
        row += " " * indent_count
        row += "*" * zigzag_width
        
        print(row)
        row = ""

        # changes the direction of the zigzag when the limit is reached for both sides
        if indent_count == 0:
            toLeft = False
        elif indent_count == base_space_count:
            toLeft = True

        # decides number of indent spaces depending on the direction of the zigzag
        if toLeft:
            indent_count -= 1
        else:
            indent_count += 1
        
        time.sleep(0.1)

# when a player clicks Ctrl + C on the keyboard, the program ends
except KeyboardInterrupt: 
    sys.exit()