__author__ = 'Anirudh'

def main():
    t = int(input())
    while t:
        s = list(input())
        l = len(s)//2
        count = 0
        while count < l:
            print(s[count], end='')
            count += 2
        print()
        t -= 1

if __name__ == '__main__': main()