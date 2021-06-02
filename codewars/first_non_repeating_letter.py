def first_non_repeating_letter(string):
    
    first = ""
    #split into individual chars
    
    chars_l = []
    for char in string:
        if char not in chars_l:
            chars_l.append(char)
    
    print(chars_l)
    
    counter = 0
    
    #we want to iterate the first char through every single character of the string passed
    
    for char in chars_l:
        for letter in string:
            if char.lower() == letter or char.upper() == letter:
                counter += 1
        if counter > 1:
            counter = 0
            continue
        else:
            first = char
            break
                    
    return first

first_non_repeating_letter("DtestEsasdA")
