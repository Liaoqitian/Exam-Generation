def all_but_first_of(s):
    return s[1:]

def all_but_last_of(s):
    return s[:len(s) - 1]

def isPalindromeAny(s):
    if len(s) < 2:
        return False 
    else: 
        if s[0] == s[len(s) - 1]:
            return True 
        else:
            return isPalindromeAny(all_but_first_of(all_but_last_of(s)))