def sh(o):
    times = 0
    while len(str(o)) != 1:
        num = 1
        times += 1
        for i in str(o):
            num *= int(i)
        o = num
    return times

i = 22222222
while 1:
    n = sh(i)
    if n >= 8:
        print(f"{i}: {n}")
    i += 1
