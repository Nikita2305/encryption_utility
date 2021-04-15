from config import *


def wrong_caesar_encrypt_args():
   print("Caesar encryption takes exactly 1 argument: int shift") 

def caesar_encrypt(filename, *args):
    if (len(args) != 1):
        wrong_caesar_encrypt_args() 
        return
    shift = 0
    try:
        shift = int(args[0])
    except ValueError:
        wrong_caesar_encrypt_args()
        return
    data = ""
    with open(filename, "r") as target_file:
        data = target_file.read()
    newdata = ""
    for i in range(len(data)):
        newdata += chr((((ord(data[i]) + shift) % utf8_module) + utf8_module) % utf8_module)
    with open(filename, "w") as target_file:
        target_file.write(newdata)
    completed_task_response()

def wrong_caesar_decrypt_args():
   print("Caesar decryption takes 0 or 1 argument: [int shift]") 

def caesar_decrypt(filename, *args):
    if (len(args) > 1):
        wrong_caesar_decrypt_args()
    if (len(args) == 0):
        print("Caesar decrypt with 0 arguments: To be developed...")
        return
    shift = 0
    try:
        shift = int(args[0])
    except ValueError:
        wrong_caesar_decrypt_args()
        return
    caesar_encrypt(filename, str(-shift))

