import sys
import json
from random import uniform
random_points = []
for i in range(10):
    x, y = uniform(-180,180), uniform(-90, 90)
    random_points.append({'longitude': x, 'latitude': y})
print(json.dumps(random_points))
sys.stdout.flush()