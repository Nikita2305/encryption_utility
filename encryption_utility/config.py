is_active = True
default_file_name = "DEFAULT_FILE_NAME"
default_mod = "DEFAULT_CRYPTO_MOD" 
utf8_module = 0x10FFFF + 1
 

def set_active(active):
    global is_active
    is_active = active

def is_active():
    global is_active
    return is_active

class Response:
   
    def __init__(self, success, value):
        self._success = success
        self._value = value
 
    @property
    def success(self):
        return self._success

    @success.setter
    def success(self, success):
        self._success = success

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

def print_response(response):
    ret = ("COMLETED with response:\n" if response.success else "FAILED with error:\n") + response.value
    print(ret)

def check_arguments(args, *types):
    if (len(types) != len(args)):
        return (False, [])
    n = len(types)
    arr = [0] * n
    for i in range(n):
        try:
            arr[i] = types[i](args[i])
        except ValueError:
            return (False, [])
    return (True, arr)
