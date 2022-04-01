def get_english_alphabet():
    return "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "

def get_english_dict(filename = "english_text.txt", block_length = 2): 
    try:
        with open(filename,"r") as f:
            data = f.read()
            d = dict() 
            alph = get_english_alphabet()
            for i in range(len(data) + 1 - block_length):
                key = data[i : i + block_length]
                ok = True
                if (i == 0):
                    for j in range(block_length - 1):
                        ok &= (key[j] in alph)
                ok &= (key[block_length - 1] in alph)
                if (ok):
                    d[key] = (d[key] if (key in d.keys()) else 0) + 1
            for key in d.keys():
                d[key] = 1000.0 * d[key] / len(data) 
            return d
    except Exception:
        raise

def count_difference(dict1, dict2):
    keys = set()
    diff = 0
    for key in dict1.keys():
        keys.add(key)
    for key in dict2.keys():
        keys.add(key)
    for key in keys:
        diff += abs((dict1[key] if (key in dict1.keys()) else 0) - (dict2[key] if (key in dict2.keys()) else 0))
    return diff
        
