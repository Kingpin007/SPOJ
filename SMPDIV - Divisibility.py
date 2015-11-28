__author__ = 'Anirudh'

def main():
    t = int(input())
    while t:
        m = list(input().split())
        n = int(m[0])
        x = int(m[1])
        y = int(m[2])
        for i in range (1,n):
            if i % x == 0 and i % y != 0:
                print(i, end=' ')
        print()
        t -= 1

if __name__ == '__main__': main()