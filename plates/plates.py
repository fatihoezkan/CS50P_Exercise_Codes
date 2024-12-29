def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() != True:
        return False

    if len(s) <2 or len(s)>6:
        return False
    for i in range(len(s)):
        if s[i].isnumeric() == True:
            a = i
            if s[a+1:len(s)+1].isnumeric() != True:
                return False
            if s[i] == "0":
                return False
            else:
                break
    for char in s:
        if char in [".",",","?","_","!"]:
            return False
    return True


main()