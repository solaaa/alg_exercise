# A B C D E , i=2 ----> D E A B C

def reverse(s):
    s_len = len(s)
    #s = list(s)
    for i in range(s_len//2):
        t = s[i]
        s[i] = s[s_len-1-i]
        s[s_len-1-i] = t
    return s

def locall_reverse(s, i):
    s = list(s)
    s[:i+1] = reverse(s[:i+1])
    s[i+1:] = reverse(s[i+1:])
    s = reverse(s)
    return ''.join(s)

print(locall_reverse('abcdef', 3))