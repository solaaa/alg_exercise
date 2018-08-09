# s1 = '1234' when s2 = '1234', '2341', '3412' or '4123', return True, else return False

# 1. s = s1 + s1 ('12341234')
# 2. KMP s with s2

def kmp_get_next(p):
    p_len = len(p)
    next_arr = [0] * p_len
    next_arr[0] = -1
    k = -1
    i = 0
    while i < p_len-1:
        if k == -1 or p[k] == p[i]:
            k += 1
            i += 1
            next_arr[i] = k
        else:
            k = next_arr[k]
    return next_arr

def kmp(s, p):
    next_arr = kmp_get_next(p)
    i = 0
    j = 0
    while i < len(s):
        if j == -1 or s[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next_arr[j]
        if j == len(p):
            return True
    return False


def is_rev_word(s1, s2):
    if len(s1) != len(s2):
        return False    
    s = s1 + s1
    return kmp(s, s2)

print(is_rev_word('1234', '3241'))
    