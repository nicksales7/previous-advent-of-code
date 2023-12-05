with open("input.txt", "r") as file:
    lst = [sorted(int(item) for item in line.strip().split("x")) for line in file]

    total_ribbon = 0
    for dimensions in lst:
        l, w, h = dimensions
        wrap = 2 * (l + w)
        bow = l * w * h 

        total_ribbon += wrap + bow
    print(total_ribbon)
