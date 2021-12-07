class Vector:
    def __init__(self, value=((0, 0), (0, 0))):
        self.value = list(value)

    def sum(self, vector2):
        self.value = [
            [self.value[0][0] + vector2.value[0][0], self.value[0][1] + vector2.value[0][1]],
            [self.value[1][0] + vector2.value[1][0], self.value[1][1] + vector2.value[1][1]]
        ]

    def deduction(self, vector2):
        self.value = [
            [self.value[0][0] - vector2.value[0][0], self.value[0][1] - vector2.value[0][1]],
            [self.value[1][0] - vector2.value[1][0], self.value[1][1] - vector2.value[1][1]]
        ]

    def multiply(self, a):
        self.value = [[self.value[0][0] * a, self.value[0][1] * a], [self.value[1][0] * a, self.value[1][1] * a]]

    def abs(self):
        return ((self.value[1][0] - self.value[0][0]) ** 2 + (self.value[1][1] - self.value[0][1]) ** 2) ** 0.5


if __name__ == "__main__":
    vect1 = Vector(((0, 0), (4, 3)))
    vect2 = Vector(((4, 3), (8, 6)))
    print(vect1.abs())
    print(vect2.abs())
    vect1.sum(vect2)
    print(vect1.abs())
    vect1 = Vector(((0, 0), (4, 3)))
    vect1.deduction(vect2)
    print(vect1.abs())
