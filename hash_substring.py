#221RDB432
# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    occurrences = []
    pattern_len = len(pattern)
    text_len = len(text)
    prime = 998244353
    prime_power = 1
    for _ in range(pattern_len - 1):
        prime_power = (prime_power * 26) % prime

    pattern_hash = 0
    text_hash = 0
    for i in range(pattern_len):
        pattern_hash = (pattern_hash * 26 + ord(pattern[i]) - ord('a')) % prime
        text_hash = (text_hash * 26 + ord(text[i]) - ord('a')) % prime

    for i in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash and pattern == text[i:i+pattern_len]:
            occurrences.append(i)

        if i < text_len - pattern_len:
            text_hash = (text_hash - (ord(text[i]) - ord('a')) * prime_power) % prime

            if text_hash < 0:
                text_hash += prime

            text_hash = (text_hash * 26 + ord(text[i+pattern_len]) - ord('a')) % prime
    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
