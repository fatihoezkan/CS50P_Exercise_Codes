l = []
name = None
while True:
    try:
        name = input("Name: ")
        l.append(name)
    except:
        print()
        break


def adieu(l):
    print("Adieu, adieu, to ", end="")
    if len(l)>2:
        for i in range(len(l)-1):
            print(f"{l[i]}, ", end="")
        print(f"and {l[len(l)-1]}")
    elif len(l)==2:
        for i in range(len(l)-1):
            print(f"{l[i]} ", end="")
        print(f"and {l[len(l)-1]}")
    elif len(l)==1:
        print(f"{l[0]} ")

adieu(l)