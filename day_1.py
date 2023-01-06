#(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
#MY ANSWER
def alphabet_position(text):
    in_array = []
    for c in text.lower():
        if c in "abcdefghijklmnopqrstuvwxyz":
            i = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'].index(c)
            in_array.append(i+1) 
    return " ".join(str(x) for x in in_array)

print(alphabet_position("The sunset sets at twelve o' clock."))
#print(alphabet_position("T"))


#BEST ANSWER
# def alphabet_position(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
