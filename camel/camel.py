s = input("camelCase: ")

for i in s:
    if i.isupper() == True:
        s = s.replace(i,f"_{i.lower()}")
        print(i)

print(s)
