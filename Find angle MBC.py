import math
def find_angle_mbc(ab, bc):
    degree = round(math.degrees(math.atan(ab/bc)))
    print(f"{degree}{chr(176)}")
if __name__ == '__main__':
    ab = int(input())
    bc = int(input())