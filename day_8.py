# Task
# Your task is to create a function that will take an integer and return the result of the look-and-say function on that integer. This should be a general function that takes as input any positive integer, and returns an integer; inputs are not limited to the sequence which starts with "1".

# Conway's Look-and-say sequence goes like this:

# Start with a number.
# Look at the number, and group consecutive digits together.
# For each digit group, say the number of digits, then the digit itself.
# Sample inputs and outputs:

# 1 is read as "one 1" => 11
# 11 is read as "two 1s" => 21
# 21 is read as "one 2, then one 1" => 1211
# 9000 is read as "one 9, then 3 0s" => 1930
# 222222222222 is read as "twelve 2s" => 122

# Your function should be able to handle numbers of arbitrary size, up to the limits of your language's arbitrary-precision integer type (if it has one). If you're working with a language that doesn't have an arbitrary-precision integer type, you may want to limit your input to a certain number of digits.  
#

def look_and_say(n):
    result = ''
    count = 1
    for i in range(len(str(n))):
        if i + 1 < len(str(n)) and str(n)[i] == str(n)[i+1]:
            count += 1
        else:
            result += str(count) + str(n)[i]
            count = 1
    return int(result)

print(look_and_say(1)) # 11
print(look_and_say(11)) # 21
print(look_and_say(21)) # 1211
print(look_and_say(9000)) # 1930