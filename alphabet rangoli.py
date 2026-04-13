import string
def print_rangoli(size):
    alphabet = string.ascii_lowercase
    rows = []
    for i in range(size):
        s = "-".join(alphabet[i:size])
        row = (s[::-1] + s[1:])
        rows.append(row.center(4 * size - 3, '-'))
    result = '\n'.join(rows[::-1] + rows[1:])
    print(result)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)