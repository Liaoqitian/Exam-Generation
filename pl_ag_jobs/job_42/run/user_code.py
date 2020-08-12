def same_values(D1, D2): 
    res = {}
    for key1 in D1: 
        for key2 in D2:
            if D1[key1] == D2[key2]:
                res[(key1, key2)] = D1[key1] 
    return res 