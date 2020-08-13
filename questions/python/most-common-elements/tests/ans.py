def most_common(sequence): 
    counts = {}
    for elem in sequence: 
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1
    max_val = max(counts.values())
    return [elem for elem in counts if counts[elem] == max_val]

def least_common(sequence): 
    counts = {}
    for elem in sequence: 
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1
    min_val = min(counts.values())
    return [elem for elem in counts if counts[elem] == min_val]