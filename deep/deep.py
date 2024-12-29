x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
x = x.strip()
if x == "42" or x.lower()=="forty two" or x.lower()=="forty-two":
    print("Yes")
else:
    print("No")