

input('input your age: ')
def dob(x, y, z):
    a = 26
    b = 6
    c = 2016
    n=(b-y)
    if x > 31:
        print('invarid data')
        return
    if y > 12:
        print('invarid data')
        return
    if n == 1:
        r = (a - x) + 31 * (b - y) + 365 * (c - z)
    elif n == 2 or n == -2:
        r = (a - x) + 61 / 2 * (b - y) + 365 * (c - z)
    elif n == -3 or n == 3:
        r = (a - x) + 92 / 3 * (b - y) + 365 * (c - z)
    elif n == -4:
        r = (a - x) + 122 / 4 * (b - y) + 365 * (c - z)
    elif n == -5:
        r = (a - x) + 153 / 5 * (b - y) + 365 * (c - z)
    elif n == -6:
        r = (a - x) + 183 / 6 * (b - y) + 365 * (c - z)
    elif n == -1:
        r = (a - x) + 30 * (b - y) + 365 * (c - z)
    elif n == 5:
        r = (a - x) + 152 / 5 * (b - y) + 365 * (c - z)
    elif n == 0:
        r = (a - x) + 365 * (c - z)
    elif n == 4:
        r = (a - x) + 121 / 4 * (b - y) + 365 * (c - z)

    print(r)
    m = (c - z) // 4
    g = r % 7
    f=(g+m)%7
    l = f // 1
    q = (c - z) / 4
    if q != m:
        l = l + 1
    if l == 0 or 1 == 7:
        print('you are born on sanday')
    if l == 1:
        print('you are born on saturday')
    if l == 2:
        print('you are born on friday')
    if l == 3:
        print('you are born on thusday')
    if l == 4:
        print('you are born on wednesday')
    if l == 5:
        print('you are born on tuesday')
    if l == 6:
        print('you are born on monday')


dob(14,10,1996)








