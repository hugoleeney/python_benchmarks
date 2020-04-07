import random


def gen_pos_numbers_inc_dec(n, up_chance=0.5, start=None):
    if not start:
        start = int(n/2)
    returned = []
    for i in range(n):
        up = random.random()
        if up<up_chance or start < 1:
            start += 1
        else:
            start -= 1
        returned.append(start)
    return returned


def gen_numbers_inc_dec(n, up_chance=0.5, start=None):
    if not start:
        start = int(n/2)
    returned = []
    for i in range(n):
        up = random.random()
        if up<up_chance:
            start += 1
        else:
            start -= 1
        returned.append(start)
    return returned


if __name__ == "__main__":
    a = gen_pos_numbers_inc_dec(20)
    print (a)
