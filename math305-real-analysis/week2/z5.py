"""Small suite of tests to check properties of Z5"""

multiply_table = [
    [0, 0, 0, 0, 0],
    [0, 1, 2, 3, 4],
    [0, 2, 4, 1, 3],
    [0, 3, 1, 4, 2],
    [0, 4, 3, 2, 1],
]

add_table = [
    [0, 1, 2, 3, 4],
    [1, 2, 3, 4, 0],
    [2, 3, 4, 0, 1],
    [3, 4, 0, 1, 2],
    [4, 0, 1, 2, 3],
]

def add_z5(a, b):
    return add_table[a][b]


def mul_z5(a, b):
    return multiply_table[a][b]


def a2():
    count = 0
    for a in range(5):
        for b in range(5):
            for c in range(5):
                assert add_z5(add_z5(a,  b), c) == add_z5(a, add_z5(b, c))
                count += 1
    print('A2 processed {c} elements'.format(c=count))


def m1():
    count = 0
    for a in range(5):
        for b in range(5):
            assert mul_z5(a, b) == mul_z5(b, a)
            count += 1
    print('M1 processed {c} elements'.format(c=count))


def m2():
    count = 0
    for a in range(5):
        for b in range(5):
            for c in range(5):
                assert mul_z5(mul_z5(a, b), c) == mul_z5(a, mul_z5(b, c))
                count += 1
    print('M2 processed {c} elements'.format(c=count))


def am1():
    count = 0
    for a in range(5):
        for b in range(5):
            for c in range(5):
                assert mul_z5(add_z5(a, b), c) == add_z5(mul_z5(a, c), mul_z5(b, c))
                count += 1
    print('AM1 processed {c} elements'.format(c=count))


if __name__ == '__main__':
    a2()
    m1()
    m2()
    am1()
    print('All assertions passed!')
