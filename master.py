def triangle(x, y, z):
    if x + y > z:
        return True
    else:
        return False


def simple(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def length_str(x):
    return len(x)


def is_int(x):
    if int(x) == x:
        return True
    else:
        return False


def anoth_sys(x, y):
    if x == 0:
        return "0"
    res = ""
    num = abs(x)

    while num > 0:
        res = str(num % y) + res
    num //= y
    return res
