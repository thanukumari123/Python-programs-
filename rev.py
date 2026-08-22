s = []
x = input("Enter string: ")
for c in x:
    s.append(c)
for i in range(len(x)):
    print(s.pop(), end=" ")