
#print ("Input the number of characters in line: ")

w = int(input("Input the number of characters in line: "))

my_string_list = ['Hello I am Phoebe!',
                   'I know you, you feed me.',
                   'You are Helen and Anton.']

def split_lines_into_words(line_list):
    new_words_list = []
    for line in line_list:
        new_words_list.extend(line.split(' '))

    return new_words_list

def generate_lines_with_new_length(accepted_lines_list, new_length):
    new_words_list = split_lines_into_words(accepted_lines_list)
    new_lines_list = []
    letters_count = 0
    current_line = ''

    for word in new_words_list:
        word_length = len(word)

        if (letters_count + word_length) < new_length:
            current_line += word + ' '
            letters_count += word_length + 1
        else:
            new_lines_list.append(current_line)
            current_line = word + ' '
            letters_count = word_length + 1
    new_lines_list.append(current_line)
    return new_lines_list

print("\n".join(generate_lines_with_new_length(my_string_list, w)))

#def cut_string(string_list, char_number):
    # i_in_curr_line = 0
    # new_string_list = []
    # new_word = ''
    # i_in_old_line = 0
    # i_in_new_line = 0
    #
    # for curr_line in my_string_list:
    #     len_curr_line = len(my_string_list[i_in_old_line])
    #
    #     if (len_curr_line <= char_number) & (new_string_list[i_in_new_line] = ' '):
    #         new_string_list[i_in_new_line] = curr_line
    #         i_in_old_line += 1
    #
    #     else:
    #         if new_string_list[i_in_new_line] != ' '):
    #             i = len_curr_line
    #         while (i_in_curr_line < len_curr_line) & (i_in_curr_line < char_number):
    #             len_word = 0
    #
    #             while (curr_line[i_in_curr_line] != ' '):
    #                 i_in_curr_line +=1
    #                 new_word += curr_line[i_in_curr_line]
    #                 len_word +=1
    #
    #             if i_in_curr_line < char_number:
    #                 new_string_list[i_in_new_line] += new_word
    #                 i_in_new_line += 1
    #
    # return new_string_list

# def cut_words(line_list):
#     words_list = []
#     #j = 0
#
#     for line in line_list:
#         len_line = len(line)
#         i = 0
#
#         while i < len_line:
#             new_word = ''
#
#             while (i < len_line) and (line[i] != ' '):
#                 new_word += line[i]
#                 i += 1
#             words_list.append(new_word)
#             #print words_list
#             i += 1
#             #j += 1
#     return words_list