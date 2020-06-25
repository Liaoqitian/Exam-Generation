def all_but_first_of(s):
    return s[1:]

def all_but_last_of(s):
    return s[:len(s) - 1]

def isPalindromeNone(s):
    if len(s) < 2:
        return True 
    else: 
        if s[0] == s[len(s) - 1]:
            return False
        else:
            return isPalindromeNone(all_but_first_of(all_but_last_of(s)))
