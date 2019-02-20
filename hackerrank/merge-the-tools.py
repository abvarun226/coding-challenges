def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        l = []
        item = string[i:i+k]
        for j in list(item):
            if j not in l:
                l.append(j)
        print("".join(l)) 


if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
