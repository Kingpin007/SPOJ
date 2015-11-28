__author__ = 'Anirudh'

def main():
    s1 = input()
    x = len(s1)
    i, j = 0, 0
    brackets_and_operations, final_result = [], []
    while i < x:
        c1 = s1[i]
        if c1 == '(':
            brackets_and_operations.append(c1)
            j += 1
        elif c1 == ')':
            brackets_and_operations.append(c1)
            index = j
            while 1:
                if brackets_and_operations[index] == ')':
                    index -= 1
                    continue
                elif brackets_and_operations[index] == '(':
                    del brackets_and_operations[index:i]
                    break
                else:
                    final_result.append(brackets_and_operations[index])
                    index -= 1
        else:
            final_result.append(c1)
        print(final_result)
        i += 1


if __name__ == '__main__':
    main()