"""ASCII String Multiplication Example"""
from ASCIIStringMultiplicationEncode import ASCIISME
from ASCIIStringMultiplicationDecode import ASCIISMD

encoded_string = ASCIISME("The quick brown fox jumps over the lazy dog")
print(encoded_string)
print(ASCIISMD(encoded_string))