#Find The Parity Outlier
#You are given an array (which will have a length of at least 3, but could be very large) containing integers. 
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single 
# integer N. Write a method that takes the array as an argument and returns this "outlier" N.
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)

#MY ANSWER
def find_outlier(integers):
    even = []
    odd = []
    for i in integers:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    if len(even) == 1:
        return even[0]
    else:
        return odd[0]

#BEST ANSWER
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]
