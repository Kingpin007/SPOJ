__author__ = 'Anirudh'

def main():
    a = list()
    while 1:
        t = int(input(''))
        a.append(t)
        a.sort()
        if len(a) >= 2:
            if a[-2] == 42:
                del a[-2]
                break

    for i in a: print(i)

if __name__ == '__main__': main()