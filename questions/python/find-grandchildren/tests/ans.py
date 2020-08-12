def find_GC(GP, PC):
    res = {}
    for key in GP:
        if GP[key] in PC:
            res[key] = PC[GP[key]]
    return res

def same_keys(D1, D2):
    res = {}
    for key in D1: 
        if key in D2:
            res[key] = (D1[key], D2[key])
    return res 

def same_values(D1, D2):
    res = {}
    for key1 in D1: 
        for key2 in D2:
            if D1[key1] == D2[key2]:
                res[(key1, key2)] = D1[key1] 
    return res 