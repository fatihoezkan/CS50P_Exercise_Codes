import random


def main():
    score = 0
    level = get_level()
    for i in range(10):
        false = 0
        x,y = generate_integer(level)
        while True:
            try:
                print(f"{x} + {y} = ", end ="")
                answer = int(input())
                if int(answer) == x + y:
                    score = score +1
                    break
                else:
                    false = false + 1
                    if false == 3:
                        print("EEE")
                        print (f"{x} + {y} = {x+y}")
                        break
                    for i in range(2):
                        print("EEE")
                        print(f"{x} + {y} = ", end ="")
                        answer = int(input())
                        if answer == x + y:
                            break
                    print (f"{x} + {y} = {x+y}")
                    break
            except:
                false = false + 1
                if false == 3:
                    print("EEE")
                    print (f"{x} + {y} = {x+y}")
                    break
                print("EEE")
                continue
    return print(f"Score: {score}")



def get_level():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
        except ValueError:
            continue
        if level > 0 and level < 4:
            break
    return level


def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
        return x,y
    if level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        return x,y
    if level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
        return x,y



if __name__ == "__main__":
    main()