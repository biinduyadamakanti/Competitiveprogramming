def get_products(inputlist):
    if len(inputlist) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')


    p= [None] * len(inputlist)


    f= 1
    for i in range(len(inputlist)):
        p[i] = f
        f*= inputlist[i]

    f= 1
    for i in range(len(inputlist) - 1, -1, -1):
        p[i] *= f
        f*= inputlist[i]

    return p


i=[int(x) for x in input().split(",")]
print(get_products(i))