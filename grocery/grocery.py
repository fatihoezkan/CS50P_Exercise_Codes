d = {}

while True:
    try:
        item = input()
        item = item.upper()
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
    except EOFError:
        for key,value in sorted(d.items()):
            print(value,key)
        break