def same_keys(D1, D2): 
    res = {}
    for key in D1: 
        if key in D2:
            res[key] = (D1[key], D2[key])
    return res 