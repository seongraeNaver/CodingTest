str = input()
list = []
for i in str:
    list.append(i)
    if 65 <= ord(i) <= 90:
        print(chr(ord(i) + 32), end = "")
    elif 97 <= ord(i) <= 122:
        print(chr(ord(i) - 32), end = "")

