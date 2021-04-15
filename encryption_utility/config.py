is_active = True
default_file_name = "DEFAULT_FILE_NAME"
default_mod = "DEFAULT_CRYPTO_MOD" 
utf8_module = 0x10FFFF + 1

def setActive(active):
    global is_active
    is_active = active

def getActive():
    global is_active
    return is_active

def wrong_encryption_mod(mods):
    print("There is no such encryption mod.")
    print("Possible are: " + ", ".join(mods))

def wrong_file_name():
    print("There is no such file")

def completed_task_response():
    print("Executed!")

