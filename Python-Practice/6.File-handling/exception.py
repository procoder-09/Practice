try:
    with open("third-file.txt","r") as f:
        print(f.read())
except FileNotFoundError:
    print("file not found")

    