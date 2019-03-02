import sys
import json

file = 'C:/Users/Shubham Tyagi/Desktop/delhi_highway.json'
with open(file, "r") as read_file:
    data = json.load(read_file)
coord = []
for line in data['features']:
    coord.append(line['geometry']['coordinates'])
new = []
for line in coord:
    for points in line:
        new.append({'lng': points[0],
                    'lat': points[1]
                    })
print(json.dumps(new))
sys.stdout.flush()
