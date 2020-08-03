def nib(n):
    if n == 0: 
        return 0
    if n == 1:
        return 2
    return nib(n - 1) + 3 * nib(n - 2)