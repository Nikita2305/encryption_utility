from encryption_utility.config import *
char_block_size = 8;
char_bits = 8;
bit_block_size = char_block_size * char_bits
spec_symbol = chr(23456)

def config(key):
    a = key // 2
    b = key ^ a
    return a, b, generate_new_key(key, a, b)

def generate_new_key(key, a, b):
    return (a * key + b) % bit_block_size

def get_utf8_bytes(char):
    value = ord(char)
    ans = ""
    for i in range(char_bits):
        new_ord = ord('0') + (value % 2) 
        ans += chr(int(new_ord))
        value /= 2;
    return ans[::-1]

def block_encrypt(filename, *args):
    option_1 = check_arguments(args, int)
    if (option_1[0]):
        key = option_1[1][0] # we assume that args are not empty
        a, b, key = config(key)
        data = ""
        with open(filename, "r") as target_file:
            data = target_file.read()
        while (len(data) % char_block_size > 0):
            data += spec_symbol;
        newdata = ""
        for i in range(len(data) // char_block_size):
            word = data[i * char_block_size : (i + 1) * char_block_size]
            bit_word = ""
            for x in word:
                bit_word += get_utf8_bytes(x) 
            new_bit_word = ""
            for i in range(len(bit_word)):
                new_bit_word += bit_word[(i + key) % bit_block_size]
            new_word = ""
            for i in range(len(new_bit_word) // char_bits):
                char_bit_str = new_bit_word[i * char_bits : (i + 1) * char_bits]
                new_word += chr(int(char_bit_str, 2))
            newdata += new_word
            key = generate_new_key(key, a, b)
        with open(filename, "w") as target_file:
            target_file.write(newdata)
        return Response(True, "New data: \"" + newdata[:10] + "...\"")
    else:
        return Response(False, "Block encryption takes exactly 1 argument: int key")

def block_decrypt(filename, *args):
    option_1 = check_arguments(args, int)
    if (option_1[0]):
        key = option_1[1][0] # we assume that args are not empty
        a, b, key = config(key)
        data = ""
        with open(filename, "r") as target_file:
            data = target_file.read()
        while (len(data) % char_block_size > 0):
            data += spec_symbol;
        newdata = ""
        for i in range(len(data) // char_block_size):
            word = data[i * char_block_size : (i + 1) * char_block_size]
            bit_word = ""
            for x in word:
                bit_word += get_utf8_bytes(x) 
            new_bit_word = ""
            for i in range(len(bit_word)):
                new_bit_word += bit_word[(i - key + bit_block_size) % bit_block_size]
            new_word = ""
            for i in range(len(new_bit_word) // char_bits):
                char_bit_str = new_bit_word[i * char_bits : (i + 1) * char_bits]
                new_word += chr(int(char_bit_str, 2))
            newdata += new_word
            key = generate_new_key(key, a, b)
        with open(filename, "w") as target_file:
            target_file.write(newdata) 
        return Response(True, "New data: \"" + newdata[:10] + "...\"")
    else:
        return Response(False, "Block decryption takes exactly 1 argument: int key")
