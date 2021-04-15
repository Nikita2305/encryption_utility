from config import *
from caesar import *
from vigenere import *
from vernam import *


def encrypt(filename = default_file_name, encryption_mod = default_mod, *args):
    encrypt_mods = {
        "caesar": caesar_encrypt,
        "vigenere": vigenere_encrypt,
        "vernam": vernam_encrypt
    } 
    try:
        target_file = open(filename, "r+")
        target_file.close()
    except FileNotFoundError:
        wrong_file_name()
        return
    if (not (encryption_mod in encrypt_mods)):
        wrong_encryption_mod(encrypt_mods)
        return
    encrypt_mods[encryption_mod](filename, *args) 

def decrypt(filename = default_file_name, decryption_mod = default_mod, *args):
    decrypt_mods = {
        "caesar": caesar_decrypt,
        "vigenere": vigenere_decrypt,
        "vernam": vernam_decrypt
    } 
    try:
        target_file = open(filename, "r+")
        target_file.close()
    except FileNotFoundError:
        wrong_file_name()
        return
    if (not (decryption_mod in decrypt_mods)):
        wrong_encryption_mod(decrypt_mods)
        return
    decrypt_mods[decryption_mod](filename, *args)

def exit(*args):
    setActive(False)

def wrong_query(commands):
    commands = list(commands)
    commands.remove("wrong_query")
    print("There is no such query.") 
    print("Possible are: " + ", ".join(commands)) 

