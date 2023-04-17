def rabin_karp(pattern, text):
    m, n = len(pattern), len(text)
    p_hash, t_hash = hash(pattern), hash(text[:m])

    for i in range(n - m + 1):
        if p_hash == t_hash and pattern == text[i:i+m]:
            print(i, end=' ')
        if i < n - m:
            t_hash = rehash(text, t_hash, i, m)
    print()

def hash(s):
    h = 0
    for c in s:
        h = (h * 26 + ord(c) - ord('a')) % 101
    return h

def rehash(s, h, i, m):
    h = (h - (ord(s[i]) - ord('a')) * (26**(m-1))) % 101
    h = (h * 26 + ord(s[i+m]) - ord('a')) % 101
    return h

pattern = str(input())
text = str(input())
rabin_karp(pattern, text)  # output: 2 5 8
