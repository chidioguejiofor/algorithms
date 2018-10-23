from modules.point import Point
from math import factorial
a = Point(3,5)
b = Point(1,8)

print(a.distance(b))

cache = {}

# def get_factorial(n):
#     if(cache.get(n)):
#         return cache.get(n)
#     value = factorial(n)
#     cache[n] = value
#     return value


# #
# # Complete the lights function below.
# #
# def lights(n):
#     #
#     # Write your code here.
#     #
#     sum =0
    
#     for number in range(1,n+1):
#         sum += get_factorial(n) // (get_factorial(n-number)* get_factorial(number))

#     mod = 10 ** 5 
#     return sum %  mod


def lights(n):
    #
    # Write your code here.
    #

    mod = 10 ** 5 
    return ((2 ** n) - 1) % mod