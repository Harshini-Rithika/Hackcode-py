def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i + k]
        unique_chars = ""
        seen = set()
        for char in substring:
            if char not in seen:
                unique_chars += char
                seen.add(char)
        print(unique_chars)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)