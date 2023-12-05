with open("input.txt", "r") as file:
    data = file.read()

    pos = 0
    for i, char in enumerate(data):
        if pos < 0:
            print(i)
            break
        if char == "(":
            pos += 1
        elif char == ")":
            pos -= 1
