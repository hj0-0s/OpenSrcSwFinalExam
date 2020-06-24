class Point:
    x = 0
    y = 0
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def distance(self, otherPoint):
        temp = 0
        temp = temp + pow(self.x-otherPoint.x,2)
        temp = temp + pow(self.y-otherPoint.y,2)
        temp = pow(temp,1/2)
        print(temp)

    def __add__(self, other):
        return [self.x + other.x, self.y + other.y]

p1 = Point(1,1)
p2 = Point(2,2)

p1.distance(p2)
print(p1 + p2)
