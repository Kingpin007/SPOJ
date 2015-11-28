import math

__author__ = 'Anirudh'


def main():
    t = int(input())
    while t:
        numbers = list(input().split())
        m = int(numbers[0])
        n = int(numbers[1])
        x = int(math.sqrt(n)) + 1
        while m < n:
            if m <= 1:
                m +=1
                continue
            elif m == 2:
                print(m)
            elif m % 2 == 0:
                m +=1
                continue
            else:
                for i in range(3, x, 2):
                    if m % i == 0:
                        m += 1
                        continue
                print(m)
            m += 1
        print()
        t -= 1


if __name__ == '__main__':
    main()