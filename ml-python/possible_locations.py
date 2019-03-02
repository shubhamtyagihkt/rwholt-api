import sys
import json
from random import uniform
random_points = []
for i in range(10):
    x, y = uniform(28.6041, 28.9041), uniform(77.0025, 77.20025)
    random_points.append({'longitude': y, 'latitude': x})
print(json.dumps(random_points))
sys.stdout.flush()
