import re

def extract_hex_colors():
    pattern = r'(?<=.)#(?:[0-9a-fA-F]{6}|[0-9a-fA-F]{3})(?![0-9a-fA-F])'
    
    import sys
    lines = sys.stdin.readlines()
    
    for line in lines:
        matches = re.findall(pattern, line)
        for match in matches:
            print(match)

if __name__ == "__main__":
    extract_hex_colors()
