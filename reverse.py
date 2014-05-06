def reverse_string(letters_list):
    list_length = len(letters_list)
    letters_list = list(letters_list)

    for i in range(0, list_length//2, 1):
        temp_letter = letters_list[i]
        letters_list[i] = letters_list[list_length - i - 1]
        letters_list[list_length - i - 1] = temp_letter

    return ''.join(letters_list)


first_string = 'ejahdjb ajebdsjb j,awbed ,ajwebdj'

#print "The reversed string: " + reverse_string(first_string)

def reverse_words(letters_list):
    list_length = len(letters_list)
    i = 0
    new_string = ''

    while i < list_length - 1:
        word = ''

        while (letters_list[i] != " ") & (i < list_length - 1):
            word += letters_list[i]
            i +=1

        if i < list_length:
            new_string += reverse_string(word) + " "
        else:
            new_string += reverse_string(word)
        i += 1

    return new_string

print "The new string with reversed words: " + reverse_words(first_string)

