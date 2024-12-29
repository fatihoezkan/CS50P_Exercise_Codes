def main():

    s = input("Input: ")

    new_s = shorten(s)

    print(new_s)

def shorten(s):
    for i in s:
        if i in ["a","e","i","o","u","A","E","I","O","U"]:
            s=s.replace(i,"")
    return s

if __name__ == "__main__":
    main()