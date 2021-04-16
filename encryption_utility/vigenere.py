from config import *

def vigenere_encrypt(filename, *args):
    option_1 = check_arguments(args, str)
    if (option_1[0]):
        shift_str = option_1[1][0] # we assume that arguments are not empty 
        data = ""
        with open(filename, "r") as target_file:
            data = target_file.read()
        newdata = ""
        for i in range(len(data)):
            shift_ind = i % len(shift_str)
            newdata += chr((((ord(data[i]) + ord(shift_str[shift_ind])) % utf8_module) + utf8_module) % utf8_module)
        with open(filename, "w") as target_file:
            target_file.write(newdata)
        return Response(True, "New data: \"" + newdata[:10] + "...\"")
    else:
        return Response(False, "Vigenere encryption takes exactly 1 argument: str key")

def vigenere_decrypt(filename, *args):
    option_1 = check_arguments(args, str)
    if (option_1[0]):
        shift_str = option_1[1][0]
        anti_shift_str = ""
        for i in shift_str:
            anti_shift_str += chr((utf8_module - ord(i)) % utf8_module)
        return vigenere_encrypt(filename, anti_shift_str)
    else:
        return Response(False, "Vigenere decryption takes exactly 1 argument: str key")
