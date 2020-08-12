def is_palindrome_all(s):
    if len(s) < 2:
        return True 
    else: 
        if s[0] == s[len(s) - 1]:
            return checkPalindrome(all_but_first_of(all_but_last_of(s)))
        else:
            return False