with open("input.txt", "r") as file:
    data = file.read()
    floor = data.count("(") - data.count(")")
    print(floor)
