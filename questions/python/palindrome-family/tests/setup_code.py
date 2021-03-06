def all_but_first_of(s):
    return s[1:]

def all_but_last_of(s):
    return s[:-1]

function = data['params']['function']

ans = {}
if data['params']['variant'] == 'all': 
    ans = {'': True, 'a': True, 'peak': False, 'abc': False, 'aabb': False, 'berkeley': False,'palindrome': False, 
    'abccba': True, 'abcba': True, 'refer': True, 'abcdedcba': True}
elif data['params']['variant'] == 'any':
    ans = {'': False, 'a': False, 'peak': False, 'c al': False, 'aabb': False, 'abcdefghi': False, 'palindrome': False, 
    'abcba': True, 'abca': True, 'refer': True, 'berkeley': True}
else:
    ans = {'': False, 'a': False, 'peak': True, 'c al': True, 'aabb': True, 'abcdefghi': True, 'palindrome': True, 
    'abcba': False, 'abca': False, 'refer': False, 'berkeley': False}
