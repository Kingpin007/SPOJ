__author__ = 'Anirudh'


def main():
    t = int(input())
    while t:
        m = list(input().split())
        l = int(m[0])*3
        c = int(m[1])*3
        pos = 0
        for j in range(l+1):
            for i in range(c+1):
                if j % 3 == 0:
                    print('*', end='')
                elif i % 3 == 0:
                    print('*', end ='')
                else:
                    print('.', end='')
            print()
        t -= 1

if __name__ == '__main__':
    main()