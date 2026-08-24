class Vector2D:
    def __init__(self,x: float,y: float):
        self.x = x
        self.y = y
    def __add__(self,other):
        self.other = other
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector2D(new_x,new_y)
    def __eq__(self,other):
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"
if __name__ == "__main__":
    v1 = Vector2D(2, 3)
    v2 = Vector2D(4, 5)

    v3 = v1+v2
    print(v3)  # Output: Vector2D(6, 8)

    v4 = Vector2D(6, 8)
    print(v3 == v4)  # Output: True