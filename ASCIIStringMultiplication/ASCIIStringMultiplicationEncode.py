"""ASCII string multiplication encryption"""
import random
import sys


def ASCIISME(string):
    #First a random number from 1 to sys.maxsize is generated. This is what ord_string will be mutliplied by
    rand_mult = random.randint(1, sys.maxsize) # this is never 0
    ord_string = ""
    
    #For every character add the length of their corresponding ascii character (2/3), 0 (for parsing) then the ascii value to a string
    for char in string:
        ord_string += str(len(str(ord(char)))) + str(0) + str(ord(char))
    
    #Multiply this large integer consisting of ascii character lengths, indicators and values by rand_mult and change it to a string, hereafter: ordstring
    ord_string_int = int(ord_string) * rand_mult
    ord_string_int_after_mult = str(ord_string_int)

    #Now we hide the value of rand_mult within the string itself
    max_len = len(ord_string_int_after_mult)
    pos_string = ""
    pos_list = []
    #For every digit in rand_mult, we pick a random position in the ordstring to insert it, we then store that position in a list
    for x in str(rand_mult):
        rand_pos = random.randint(1, max_len)
        while (rand_pos in pos_list):
            rand_pos = random.randint(1, max_len)
        pos_list.append(rand_pos)
        #Because the length and thus position of digits changes as they're being added, should the insertion of one digit affect another, it is updated accordingly
        for y in range(len(pos_list) - 1):
            if (rand_pos < pos_list[y]):
                pos_list[y] += 1
        ord_string_int_after_mult = ord_string_int_after_mult[:(rand_pos - 1)] + x + ord_string_int_after_mult[(rand_pos - 1):]  
    
    #We then construct a string that is placed at the beginning of the ordstring as a way for the decryption algorithm to determine what value the ordstring was multiplied by, hereafter: posstring
    #We do this in a similar to the ascii values above
    for x in pos_list:
        pos_string += str(len(str(x))) + str(0) + str(x) 

    #We then set the posstring to be the length of the posstring, then the 0 indicator, then the posstring
    pos_string = str(len(pos_string)) + str(0) + pos_string
   
    #We then combine the posstring and the ordstring together, this is the encrypted message
    ord_string_int_after_mult = pos_string + ord_string_int_after_mult

    return ord_string_int_after_mult        
