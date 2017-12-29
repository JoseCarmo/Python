
"""If a circle of radius R is inscribed inside a square with side length 2R, 
then the area of the circle will be pi*R^2 and the area of the square will be (2R)^2. 
So the ratio of the area of the circle to the area of the square will be pi/4.

This means that, if you pick N points at random inside the square, approximately N*pi/4 
of those points should fall inside the circle.

This program picks points at random inside the square. It then checks to see if the point 
is inside the circle (it knows it's inside the circle if x^2 + y^2 < R^2, where x and y
are the coordinates of the point and R is the radius of the circle). The program keeps 
track of how many points it's picked so far and how many of those points fell inside 
the circle. """

import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

NumberOfPoints = 150000
PointLocationX = []
PointLocationY = []
PointLocationINx = []
PointLocationINy = []
PointLocationOUTx = []
PointLocationOUTy = []
SquareSide = 10


for interations in range(0, NumberOfPoints):
    PointLocationX.append(float(random.uniform(-SquareSide/2, SquareSide/2)))
    PointLocationY.append(float(random.uniform(-SquareSide/2, SquareSide/2)))
    if (  pow((PointLocationX[interations]),2) + pow((PointLocationY[interations]),2) <= pow(SquareSide/2, 2)):
      PointLocationINx.append(PointLocationX[interations])
      PointLocationINy.append(PointLocationY[interations])
    else:
      PointLocationOUTx.append(PointLocationX[interations])
      PointLocationOUTy.append(PointLocationY[interations])
    
plt.plot(PointLocationINx, PointLocationINy, 'ro', PointLocationOUTx, PointLocationOUTy, 'go')
print(4*len(PointLocationINx)/NumberOfPoints) # here is the pi estimative calculation 
plt.show()
