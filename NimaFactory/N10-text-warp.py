print('N10-text-warp V1.0 running...\n')
print('enter a string and a number for warp')
print('for example : abcdefghi for string and 3 for number')
print('abc')
print('efg')
print('hi\n')


def wrap(string, max_width):
    res = string
    counter = 0
    counter_index = 0
    for i in string:
        counter_index += 1
        if counter_index % max_width == 0:
            counter += 1
        string = string[1:]
    counter_list = [x * max_width for x in range(1, counter + 2)]
    for i in range(len(res), max_width - 1, -1):
        if i in counter_list:
            res = res[:i] + '\n' + res[i:]
    return res


if __name__ == '__main__':
    string, max_width = input('enter a string : '), int(input('enter a number : '))
    result = wrap(string, max_width)
    print(result)
