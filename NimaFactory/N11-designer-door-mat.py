print('N11-designer-door-mat V1.0 running...\n')
print('enter a number for height and see result')
print('it created for odd numbers (you can use even but i don\'t suggest)')
print('for example : 7\n')
print('''---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------\n\n''')
# it was for hackerrank
# -------------------------
# size = input()
# size = size.split(' ')
# n = int(size[0])
# m = int(size[1])
# -------------------------
size = input('enter a number : ')
n = int(size)
m = int(size) * 3
welcome = 'WELCOME'
n_center = int((n - 1) / 2)
down_helper = {'center': 0, 'min_m': 0}


def up(n_center, m):
    counter = 1
    m = int((m - (counter * 3)) / 2)
    for i in range(n_center):
        nima_1 = counter * '.|.'
        nima_2 = m * '-'
        print(nima_2 + nima_1 + nima_2)
        counter += 2
        m -= 3
    down_helper.update({'center': counter, 'min_m': m})


def center(m):
    m -= 7
    m = int(m / 2)
    nima_2 = m * '-'
    print(nima_2 + welcome + nima_2)


def down(down_helper):
    counter = down_helper.get('center') - 2
    m = down_helper.get('min_m') + 3
    for i in range(n_center):
        nima_1 = counter * '.|.'
        nima_2 = m * '-'
        print(nima_2 + nima_1 + nima_2)
        counter -= 2
        m += 3


up(n_center, m)
center(m)
down(down_helper)
