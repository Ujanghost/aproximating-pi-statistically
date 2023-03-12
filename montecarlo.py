import random

def is_inside_square(x, y, a):
    return abs(x) <= a/2 and abs(y) <= a/2

def is_inside_circle(x, y, a):
    return x**2 + y**2 <= (a/2)**2

a = 1   # side length of the square, and radius of the circle
num_points = 100000

count_square = 0
count_circle = 0
for i in range(num_points):
    x = random.uniform(-a/2, a/2)
    y = random.uniform(-a/2, a/2)
    if is_inside_square(x, y, a):
        count_square += 1
    if is_inside_circle(x, y, a):
        count_circle += 1

ratio = count_circle / count_square
print("Ratio of marbles in square to marbles in circle:", ratio)
print("Value of pi apx pi:", ratio*4)
