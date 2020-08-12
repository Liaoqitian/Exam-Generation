def twin_remover(A, B):
    if A == "":
        return []
    elif B == "":
        return [] 
    elif A[0] == B[0]: ### 1st letter of A is equal to 1st letter of B
        return twin_remover(A[1:], B[1:])
    else:
        return [(A[0], B[0])] + twin_remover(A[1:], B[1:])

def twin_keeper(A, B):
    if A == "":
        return []
    elif B == "":
        return [] 
    elif A[0] == B[0]: ### 1st letter of A is equal to 1st letter of B
        return [(A[0], B[0])] + twin_keeper(A[1:], B[1:])
    else:
        return twin_keeper(A[1:], B[1:])

def twin_counter(A, B): 
    if A == "":
        return 0
    elif B == "": 
        return 0
    elif A[0] == B[0]: ### 1st letter of A is equal to 1st letter of B
        return 1 + twin_counter(A[1:], B[1:])
    else:
        return twin_counter(A[1:], B[1:])

def singleton_counter(A, B): 
    if A == "":
        return 0
    elif B == "": 
        return 0
    elif A[0] == B[0]: ### 1st letter of A is equal to 1st letter of B
        return singleton_counter(A[1:], B[1:])
    else:
        return 1 + singleton_counter(A[1:], B[1:])