class Text:
    def __init__(self, text):
        self.text = text
        self.x = 0
        self.y = 0
        self.visited_houses = {(0, 0)}

    def sort_text(self):
        return list(self.text.replace("\n", "")) 

    def update_position(self, direction):
        if direction == "^":
            self.y += 1
        elif direction == "v":
            self.y -= 1
        elif direction == ">":
            self.x += 1
        elif direction == "<":
            self.x -= 1

    def visit_house(self):
        for char in self.sort_text():
            self.update_position(char)
            self.visited_houses.add((self.x, self.y))

    def count_houses(self):
        return len(self.visited_houses)

with open("input.txt", "r") as file:
    text = Text(file.read())
    text.visit_house()
    print(text.count_houses())
     
