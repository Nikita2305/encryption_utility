from config import *
from frequency_analysis import *
import os
import random

def caesar_encrypt(filename, *args):
    option_1 = check_arguments(args, int)
    if (option_1[0]): 
        shift = option_1[1][0]
        data = ""
        with open(filename, "r") as target_file:
            data = target_file.read()
        newdata = ""
        for i in data:
            newdata += chr((((ord(i) + shift) % utf8_module) + utf8_module) % utf8_module)
        with open(filename, "w") as target_file:
            target_file.write(newdata)
        return Response(True, "New data: \"" + newdata[:10] + "...\"")
    else:
        return Response(False, "Caesar encryption takes exactly 1 argument: int key")

def caesar_decrypt(filename, *args):
    option_1 = check_arguments(args, int)
    option_2 = check_arguments(args)
    if (option_1[0]):
        shift = option_1[1][0]
        return caesar_encrypt(filename, str(-shift))
    elif (option_2[0]):
        basic_dict = dict()
        try:
            basic_dict = get_english_dict("english_text.txt")
        except Exception:
            return Response(False, "Frequency analysis module failed.")
        data = ""
        with open(filename, "r") as target_file:
            data = target_file.read()
        
        best_diff = 10**10
        best_shift = 0
        temp_filename = ".tempfile"
        for i in range(20):
            pos = random.randint(0, len(data) - 1)
            for char in get_english_alphabet():
                shift = ord(char) - ord(data[pos])
                with open(temp_filename,"w") as temp:
                    temp.write(data)
                caesar_encrypt(temp_filename, str(shift))
                custom_dict = get_english_dict(temp_filename) 
                diff = count_difference(basic_dict, custom_dict)
                os.remove(temp_filename)
                if (diff < best_diff):
                    best_diff = diff
                    best_shift = shift
        transcription_filename = filename + ".scrp"
        with open(transcription_filename, "w") as transcr_file:
            transcr_file.write(data)
        caesar_encrypt(transcription_filename, str(best_shift))
        return Response(True, "Transcription was written to " + transcription_filename)
    else:
        return Response(False, "Caesar decryption takes 0 or 1 argument: [int key]")
