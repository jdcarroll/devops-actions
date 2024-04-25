import sys

for item in sys.argv:
    if ',' in item:
        data = item.split(',')

print(data)
