# ['abc', 'de'] ---> 'abcde'    ('deabc' X) 

def is_bigger(s1, s2):
    t1 = s1 + s2
    t2 = s2 + s1
    for i in range(len(t1)):
        if t1[i] == t2[i]:
            continue
        if t1[i] < t2[i]:
            # s1 < s2
            return False
        else:
            # s1 > s2
            return True
    return False

def patition(s, l, r):
    #r = len(s)-1
    if l >= r:
        return s
        
    i = l-1
    j = l
    while j < r:
        if is_bigger(s[j], s[r]) == True:
            j += 1
        else:
            i += 1
            t = s[i]
            s[i] = s[j]
            s[j] = s[i]
            j += 1
    i += 1 

    t = s[i]
    s[i] = s[r]
    s[r] = t
    
    s = patition(s, l, i-1)
    s = patition(s, i+1, r)
    
    return s

def sort(s):
    s = patition(s, 0, len(s)-1)
    return s

print(sort(['op', 'acb', 'df', 'abc']))
