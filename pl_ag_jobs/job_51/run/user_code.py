def find_GC(GP, PC): 
    res = {}
    for key in GP:
        if GP[key] in PC:
            res[key] = PC[GP[key]]
    return res