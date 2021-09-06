"""ASCII string multiplication encryption"""
def ASCIISMD(intt):
    #The first step for decrypting ASCII string multiplication is to find the value that the ordstring was multiplied by
    #This is done by parsing the posstring which is always positioned at the beginning of the encrypted string
    ind = 0
    pos_string_len = ""
    
    #First determine the posstrings length
    while(True):
        if intt[ind] == '0' and intt[ind + 1] != '0':
            break
        else:
            pos_string_len += str(intt[ind])
            ind += 1
    ind += 1

    #Now determine the position of every digit of the multiplier in the ordstring
    counter = 0
    counter_str = ""
    curr_pos = ""
    pos_list = []
    for x in range(int(pos_string_len)):
        if (counter == 0):
            if (len(curr_pos) != 0):
                pos_list.append(int(curr_pos))
            curr_pos = ""
            if intt[ind + x] == '0' and intt[ind + x + 1] != '0':
                counter = int(counter_str)
                counter_str = ""
            else:
                counter_str += intt[ind + x]
        else:
            curr_pos += intt[ind + x]
            counter -= 1
    pos_list.append(int(curr_pos))    
    
    #Now that we've determined the position of every digit within the ordstring, we don't need the posstring so we can discard it
    ind += int(pos_string_len)
    decode_str = intt[ind:]
    
    #Retrieve every digit corresponding to a position in the ordstring and combine them together into a string
    mult_int_str = ""
    for pos in pos_list:
        mult_int_str += decode_str[pos - 1]

    #We sort the position list in reversed order as we know want to remove them from the ordstring
    pos_list.sort(reverse=True)
    
    #Why is the list reversed? Everytime we remove a character from the ordstring, the relative position of all characters in front of it gets changed by 1
    #By sorting the list in descending order, we ensure that everytime we remove a character that none of the positions of the characters we still need to remove change
    
    #Now remove all of those characters from the ordstring
    for pos in pos_list:
        decode_str = decode_str[:pos - 1] + decode_str[pos:]
    
    #Divide the integer value of the ordstring by the integer value of the multiplier that we just determined
    decode_int_string = int(decode_str) // int(mult_int_str)
    
    #Now retrieve the ASCII values that are now easy for us to retrieve from the ordstring
    counter = 0
    counter_str = ""
    curr_pos = ""
    char_list = []
    for x in range(len(str(decode_int_string))):
        if (counter == 0):
            if (len(curr_pos) != 0):
                char_list.append(int(curr_pos))
            curr_pos = ""
            if str(decode_int_string)[x] == '0' and str(decode_int_string)[x + 1] != '0':
                counter = int(counter_str)
                counter_str = ""
            else:
                counter_str += str(decode_int_string)[x]
        else:
            curr_pos += str(decode_int_string)[x]
            counter -= 1
    char_list.append(int(curr_pos))    

    #Convert all the ASCII values back to their character values are return the result
    decoded_string = ""
    for char in char_list:
        decoded_string += chr(char)
    
    return decoded_string