def nib(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return 3 * nib(n - 2) + 2 * nib(n - 1)