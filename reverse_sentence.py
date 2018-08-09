# input: 'pigs love dogs' ---> output: 'dogs love pigs'

def reverse(s):
    s_len = len(s)
    s = list(s)
    for i in range(s_len//2):
        t = s[i]
        s[i] = s[s_len-1-i]
        s[s_len-1-i] = t
    return ''.join(s)

def reverse_sentence(s):
    s = reverse(s)
    s = s.split(' ')
    s = [reverse(string) for string in s]
    return ' '.join(s)

print(reverse_sentence('pigs love dogs'))