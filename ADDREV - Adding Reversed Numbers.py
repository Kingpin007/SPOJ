__author__ = 'Anirudh'


def main():
    t =int(input())
    while t:
        nums = list(input().split())
        x = nums[0]
        y = nums[1]
        x = int(x[::-1])
        y = int(y[::-1])
        s = str(x+y)
        s = s.strip('0')
        print(s[::-1])
        t -= 1

if __name__ == '__main__': main()