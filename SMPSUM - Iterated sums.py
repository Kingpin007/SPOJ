__author__ = 'Anirudh'


def main():
    x = list(input().split())
    a = int(x[0])
    b = int(x[1])
    s = 0
    while a <= b:
        s += a*a
        a += 1
    print(s)

if __name__ == '__main__':
    main()