from point import Point
from functools import reduce

class Cluster:

    def __init__(self, x,y):
        self.center = Point(x,y)
        self.points = [self.center]

    def update_center(self):
        x_total = reduce(lambda x,point: x + point.x, self.points, 0)
        y_total = reduce(lambda y,point: y + point.y, self.points, 0)
        self.center.x = x_total / len(self.points)
        self.center.y = y_total / len(self.points)

    def add_point(self, x,y):
        self.points.append(Point(x,y))
        self.update_center();


if __name__ =='__main':
    print(Cluster(1,0))
    