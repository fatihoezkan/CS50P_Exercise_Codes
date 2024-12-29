x = input("File Name: ")
x= x.strip()
x= x.lower()

if x[-3:] == "gif":
    print("image/gif")
elif x[-3:] == "jpg" or x[-4:] == "jpeg" :
    print("image/jpeg")
elif x[-3:] == "png":
    print("image/png")
elif x[-3:] == "pdf":
    print("application/pdf")
elif x[-3:] == "txt":
    print("text/plain")
elif x[-3:] == "zip":
    print("application/zip")
else:
    print("application/octet-stream")
