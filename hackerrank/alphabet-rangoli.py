

def get_prev_char(c):
    return chr(ord(c) - 1)

def reverse(string):
    string = string[::-1]
    return string

def print_rangoli(size):
    if size == 1:
        print('a')
        return

    n = chr(ord('a') + size - 1)
    cols = (((size - 1) * 2) * 2) + 1
    rows = size + (size - 1)

    stack = []
    for i in range(int(rows/2) + 1):
        m = n
        l = n
        j = i
        while j > 0:
            l = get_prev_char(l)
            j -= 1
            m += "-" + l
        m += "-" + reverse(m[:len(m)-2])
        t = m.center(cols, "-")
        print(t)
        if i < int(rows/2):
            stack.append(t)
    while len(stack) > 0:
        print(stack.pop())


if __name__ == '__main__':
    n = int(raw_input())
    print_rangoli(n)
