import math
__author__ = 'Anirudh'


def main():
    t = int(input())
    while t:
        x = int(input())
        j, s = 1, 0
        max = math.sqrt(x)
        if x != 1:
            while j <= max:
                if x % j == 0:
                    s += j + (x//j)
                j += 1
        else:
            print(0)
            continue
        print(s-x)
        t -= 1

if __name__ == '__main__': main()