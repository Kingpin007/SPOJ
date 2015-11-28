__author__ = 'Anirudh'


def main():
    t = int(input())
    while t:
        m = list(input().split())
        l = int(m[0])
        c = int(m[1])
        pos = 0
        for j in range(l):
            for i in range(c):
                if pos % 2 == 0:
                    print ('*', end='')
                    pos += 1
                else:
                    print('.', end='')
                    pos += 1
            if c % 2 == 0:
                pos += 1
            print()
        t -= 1

if __name__ == '__main__':
    main()