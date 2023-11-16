import math
perimeter=0
x0=float(input('Enter the x part of the coordinate: '))
y0=float(input('Enter the y part of the coordinate: '))
while True:
    x_str=input('Enter the x part of the coordinate: (blank to quit): ')
    if not x_str:
        break
    x=float(x_str)
    y=float(input('Enter the y part of the coordinate: '))
    distance=math.sqrt((x-x0)**2 + (y-y0)**2)+(x-x0)+(y-y0)
    perimeter+=distance
    x0=x
    y0=y
print('The perimeter of that polygon is',perimeter)
