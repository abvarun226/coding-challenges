import itertools

def decodeString(s: str) -> str:
    result = ''
    i = 0
    while i < len(s):
        cur_char = s[i]
        if cur_char.isdigit():
            k = int(''.join(list(itertools.takewhile(lambda x: x.isdigit(), s[i:]))))
            i += len(str(k))

            stack = []
            count = 0
            for v in s[i+1:]:
                count += 1
                if v == '[':
                    stack.append(v)
                elif v == ']':
                    if len(stack) == 0:
                        break
                    stack.pop()
            chunk = s[i+1:i+count]
            decoded_chunk = decodeString(chunk)
            result += k * decoded_chunk
            i += count + 1
        else:
            result += cur_char
            i += 1

    return result


inp = ["3[a]2[bc]", "3[a2[c]]", "2[abc]3[cd]ef"]
exp = ["aaabcbc", "accaccacc", "abcabccdcdcdef"]
for i, v in enumerate(inp):
    act = decodeString(v)
    assert exp[i] == act, 'expected {0} != actual {1}'.format(exp[i], act)