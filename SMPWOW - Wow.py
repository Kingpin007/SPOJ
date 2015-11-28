__author__ = 'Anirudh'


def main():
    x = int(input())
    print('W', end='')
    j = 0
    while j < x:
        print('o', end='')
        j += 1
    print('w')

if __name__ == '__main__': main()