def possibilities(signals):
    morse_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--.."
    }
    unknown_count = signals.count("?")
    possible_chars = []
    if unknown_count == 0:
        if signals in morse_dict.values():
            possible_chars.append([k for k, v in morse_dict.items() if v == signals][0])
    elif unknown_count == 1:
        for char, code in morse_dict.items():
            for i in range(len(code)):
                if code[i] == "?" or code[i] == signals[i]:
                    possible_chars.append(char)
                    break
    else:
        possible_chars = [char for char in morse_dict.keys()]
    return sorted(possible_chars)

