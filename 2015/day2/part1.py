with open("input.txt", "r") as file:
    lst = [sorted(int(item) for item in line.strip().split("x")) for line in file]

    surface_area_total = 0
    for dimensions in lst:
        # 2*l*w + 2*w*h + 2*h*l (l->w->h)
        l, w, h = dimensions
        surface_area = 2 * l * w + 2 * w * h + 2 * h * l

        slack = l * w

        surface_area_total += surface_area + slack
    print(surface_area_total)
