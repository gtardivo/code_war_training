#Printer Errors
# s="aaabbbbhaijjjm"
# printer_error(s) => "0/14"
# s="aaaxbbbbyyhwawiwjjjwwm"
#printer_error(s) => "8/22"


def printer_error(s):
    # your code
    return str(len([x for x in s if x not in "abcdefghijklm"])) + "/" + str(len(s))
