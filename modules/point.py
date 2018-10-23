
class Point: 
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point):
        if isinstance(point, Point):
            x_squared = (self.x - point.x) ** 2
            y_squared = (self.y - point.y) ** 2
            squared_sum = x_squared + y_squared
            return squared_sum  ** 0.5
        return 0
    
    
            