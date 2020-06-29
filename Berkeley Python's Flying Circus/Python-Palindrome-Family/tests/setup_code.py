def all_but_first_of(s):
    return s[1:]

def all_but_last_of(s):
    return s[:-1]

ans = {}
if data['params']['variant'] == 'All': 
    ans = {'': True, 'a': True, 'peak': False, 'abc': False, 'aabb': False, 'berkeley': False,'palindrome': False, 
    'abccba': True, 'abcba': True, 'refer': True, 'abcdedcba': True}
elif data['params']['variant'] == 'Any':
    ans = {'': True, 'a': True, 'peak': True, 'c al': False, 'aabb': False, 'abcdefghi': False, 'palindrome': False, 
    'abcba': True, 'abca': True, 'refer': True, 'berkeley': True}
else:
    ans = {'': False, 'a': False, 'peak': True, 'c al': True, 'aabb': True, 'abcdefghi': True, 'palindrome': True, 
    'abcba': False, 'abca': False, 'refer': False, 'berkeley': False}
