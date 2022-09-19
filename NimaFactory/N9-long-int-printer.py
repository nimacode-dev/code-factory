print('N9-long-int-printer V1.0 running...')
print('(without using any string (only used for print messages))\n')
print('enter an number and see the result!')
print('for example you entered 15')
print('result : 123456789101112131415\n')
# from math import log10
# # 123 >>> what I want >>> 3
# a = log10(123) # 2.xxxxxx
# a = int(a) + 1
# print(a) # I want this

if __name__ == '__main__':
    from math import log10
    n = int(input('enter a number : '))
    nima = []
    res_n = 0
    res_nima = 0
    for i in range(n, 0, -1):
        res = (10 ** res_n) * i
        res_n += int(log10(i)) + 1
        nima.append(res)
    for i in nima:
        res_nima += i
    print(res_nima)
