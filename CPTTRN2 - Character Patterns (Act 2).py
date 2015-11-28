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
                if j == 0 or j == l-1:
                    print('*', end='')
                elif i==0 or i == c-1:
                    print('*', end ='')
                else:
                    print('.', end='')
            print()
        t -= 1

if __name__ == '__main__':
    main()