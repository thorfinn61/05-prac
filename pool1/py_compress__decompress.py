def compress(s: str) -> str:
    result = ""
    i = 0
    while i < len(s):
        count = 1
        while i + count < len(s) and s[i] == s[i + count]:
            count += 1
        result += s[i] + str(count if count > 1 else "")
        i += count
    return result

def decompress(s: str) -> str:
    result = ""
    i = 0
    while i < len(s):
        char = s[i]
        i += 1
        digits = ""
        while i < len(s) and s[i].isdigit():
            digits += s[i]
            i +=1
        result += char * int(digits or 1)
    return result

if __name__ == "__main__":
    print(compress("aabcccccaaa"))
    print(decompress("a2bc5a3"))
    print(compress("abc"))
    print(compress("aaaaaaaaaaaa"))
    print(decompress("a12b"))
    print(compress(""))