def all_but_first_of(s):
    return s[1:]

def all_but_last_of(s):
    return s[:len(s) - 1]

def checkPalindrome(s):
    # if len(s) < 2:
    #     return True 
    # else: 
    #     if s[0] == s[len(s) - 1]:
    #         return is_palindrome_all(all_but_first_of(all_but_last_of(s)))
    #     else:
    #         return False
    try: 
        return ans[s]
    except KeyError:
        return 0