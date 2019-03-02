import sys
import json
import numpy as np

file = 'ml-python/delhi_highway.json'
with open(file, "r") as read_file:
    data = json.load(read_file)

coord = []
for line in data['features']:
    coord.append(line['geometry']['coordinates'])
	
new = []
for line in coord:
    for points in line:
        new.append(points)
new_np = np.unique(np.array(new),axis=0)
new = []
for line in new_np:
    new.append({'lng': line[0],
                'lat': line[1]
    }) 
print(json.dumps(new))
sys.stdout.flush()
