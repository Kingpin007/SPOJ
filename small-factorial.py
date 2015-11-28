__author__ = 'Anirudh'

def main():
    t = int(input())
    while t:
        n = int(input())
        res = 1
        while n >= 1:
            res *= n
            n -= 1
        print(res)
        t -= 1

if __name__ == '__main__': main()