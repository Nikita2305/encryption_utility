from encryption_utility.config import *
local_vernam_module = 2 ** 20


def vernam_encrypt(filename, *args):
    option_1 = check_arguments(args, str)
    if (option_1[0]):
        key_str = option_1[1][0] # we assume that args are not empty
        data = ""
        with open(filename, "r") as target_file:
            data = target_file.read()
        newdata = ""
        for i in range(len(data)):
            key_ind = i % len(key_str)
            newdata += chr((ord(data[i]) % local_vernam_module) ^ (ord(key_str[key_ind]) % local_vernam_module)) 
        with open(filename, "w") as target_file:
            target_file.write(newdata)
        return Response(True, "New data: \"" + newdata[:10] + "...\"")
    else:
        return Response(False, "Vernam encryption takes exactly 1 argument: str key")

def vernam_decrypt(filename, *args):
    option_1 = check_arguments(args, str)
    if (option_1[0]):
        key_str = option_1[1][0]
        return vernam_encrypt(filename, key_str) 
    else:
        return Response(False, "Vernam decryption takes exactly 1 argument: str key")
