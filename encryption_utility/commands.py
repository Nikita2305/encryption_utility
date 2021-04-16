from config import *
from caesar import *
from vigenere import *
from vernam import *


def wrong_encryption_mod_error(mods):
    return Response(False, "There is no such encryption mod.\nPossible are: " + ", ".join(mods))

def wrong_file_name_error():
    return Response(False, "There is no such file or multiaccess was denied.")

def encrypt(filename = default_file_name, encryption_mod = default_mod, *args):
    encrypt_mods = {
        "caesar": caesar_encrypt,
        "vigenere": vigenere_encrypt,
        "vernam": vernam_encrypt
    } 
    try:
        target_file = open(filename, "r+")
        target_file.close()
    except Exception:
        return wrong_file_name_error()
    if (not (encryption_mod in encrypt_mods)): 
        return wrong_encryption_mod_error(encrypt_mods)
    return encrypt_mods[encryption_mod](filename, *args) 

def decrypt(filename = default_file_name, decryption_mod = default_mod, *args):
    decrypt_mods = {
        "caesar": caesar_decrypt,
        "vigenere": vigenere_decrypt,
        "vernam": vernam_decrypt
    } 
    try:
        target_file = open(filename, "r+")
        target_file.close()
    except Exception: 
        return wrong_file_name_error()
    if (not (decryption_mod in decrypt_mods)): 
        return wrong_encryption_mod_error(decrypt_mods)
    return decrypt_mods[decryption_mod](filename, *args)

def exit(*args):
    set_active(False)
    return Response(True, "Thank you for using our utility!")

def wrong_query(commands = [], *args):
    commands = list(commands)
    commands.remove("wrong_query")
    return Response(False, "There is no such query.\nPossible are: " + ", ".join(commands))

