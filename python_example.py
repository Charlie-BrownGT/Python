import random
import math

points_used = 1000000
i = 0
x = 0
y = 0
distance_squared = 0
inside_circle = 0
outside_circle = 0
pi = 0

while(i < points_used):

    x = random.random()
    y = random.random()
    
    distance_squared = x**2 + y**2

    if distance_squared <= 1:
        inside_circle = inside_circle + 1
    else:
        outside_circle = outside_circle + 1
    i=i + 1
    
pi = 4 * (inside_circle / points_used)
print(pi)