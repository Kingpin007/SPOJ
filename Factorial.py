__author__ = 'Anirudh'


def main():
    lines = int(input())
    while lines:
        number = int(input())
        s = 0
        while number > 0:
            s += number//5
            number //= 5
        print(s)
        lines -= 1

if __name__ == '__main__':
    main()