def same_values(D1, D2): 
    res = {}
    for key in GP:
        if GP[key] in PC:
            res[key] = PC[GP[key]]
    return res