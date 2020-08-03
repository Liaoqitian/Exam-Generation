def nib(n):
    if n == 0: 
        return -1 
    if n == 1:
        return 3
    return 2 * nib(n - 1) + nib(n - 2)