#221RDB432
# python3

def read_input():
    inputLetter = input().strip().upper()
    if inputLetter == "I":
        inputPattern = input().strip()
        inputText = input().strip()
        return inputLetter, inputPattern, inputText
    elif inputLetter == "F":
        fileName = 'tests/06'
        with open(fileName) as file:
            inputPattern = file.readline().strip()
            inputText = file.readline().strip()
            return inputLetter, inputPattern, inputText
    else:
        print("try again")
        exit()

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(input_vers, pattern, text):
    text_len = len(text)
    pattern_len = len(pattern)
    occurrences = []

    if input_vers == "I":
        for i in range(text_len -pattern_len + 1):
            if text[i: i + pattern_len] == pattern:
                occurrences.append(i)
    elif input_vers == "F":
        pattern_hash = 0
        text_hash = 0
        for i in range(pattern_len):
            pattern_hash += ord(pattern[i]) * pow(10, pattern_len - i - 1)
            text_hash += ord(text[i]) * pow(10, pattern_len - i - 1)         
        
        for i in range(text_len - pattern_len + 1):
            if text_hash == pattern_hash:
                if text[i:i + pattern_len] == pattern:
                    occurrences.append(i)
            
            if i < text_len - pattern_len:
                text_hash = (text_hash - ord(text[i]) * pow(10, pattern_len - 1)) * 10 + ord(text[i + pattern_len])                
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
