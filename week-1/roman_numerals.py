'''Roman Numerals

I	1	
V	5	
X	10	
L	50	
C	100	
D	500	
M	1,000

25 = XXV
4 = IV


Will fix sometime later
'''



roman_numerals_int = [1000, 500, 100, 50, 10, 5, 1]
roman_numerals_letter = ['M', 'D', 'C', 'L', 'X', 'V', 'I']


while True:
    answer = ""
    numerals = []
    x = int(input("\nEnter number from 1 - 3999: "))

    #iterate through every roman numeral
    for rn in roman_numerals_int:  

        # if the current roman numeral is less than x
        if x >= rn: 
            for i in range(0, int(x / rn)): 
                numerals.append(rn)

            # get remainder and make this the new value
            x = x % rn 

    print(numerals)


    # convert numerals list to string
    for i in range(0, len(roman_numerals_int)):
        number = roman_numerals_int[i]
        letter = roman_numerals_letter[i]

        if numerals.count(number) == 4:
            letter = letter + roman_numerals_letter[i - 1]
            answer += letter
        else:
            answer += letter * numerals.count(number)

    print(answer)


'''


def count_occurrence(numerals, num):
    count = 0
    for n in numerals:
        if n == num:
            count += 1
    return count
'''