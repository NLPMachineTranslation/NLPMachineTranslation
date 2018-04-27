
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

print("Point A:")
print("Enter x1: ")
x1 = int(input())
print("Enter y1: ")
y1 = int(input())

print("Point B:")
print("Enter x2: ")
x2 = int(input())
print("Enter y2: ")
y2 = int(input())

num = y2-y1
denom = x2-x1

num = abs(num)
denom = abs(denom)
print("NUM: %s" %num)
print("DEN: %s" %denom)

slope = float(num/denom)
print("SLP: %s" %slope)

x = []
y = []
z = []

w = 0
h = 0
#len(x) == len(y)

if num < denom:
    print("X")
    if x1 < x2:
        w = x2+1
        for i in range(x1, x2+1):
            x.append(i)
        print(x)
    else:
        w = x1+1
        for i in range(x1, x2-1, -1):
            x.append(i)
        print(x)
    if(y1 > y2):
        h = y1+1
        y.append(y1)
        z.append(y1)
        yB = 0
        print("Y")
        for i in range(0, len(x) - 2):
            if slope < 1:
                yB = z[i] - slope
                print(yB)
            else:
                yB = z[i] - 1/slope
                print(yB)
            z.append(yB)
            y.append(round(yB,))
        y.append(y2)
        print(y)
    else:
        h = y2+1
        y.append(y1)
        z.append(y1)
        yB = 0
        print("Y")
        for i in range(0, len(x) - 2):
            if slope < 1:
                yB = z[i] + slope
                print(yB)
            else:
                yB = z[i] + 1/slope
                print(yB)
            z.append(yB)
            y.append(round(yB,))
        y.append(y2)
        print(y)
########################################################################
else:
    if y1 < y2:
        h = y2+1
        for j in range(y1, y2+1):
            y.append(j)
        print(y)
    else:
        h = y1+1
        for j in range(y1, y2-1, -1):
            y.append(j)
        print(y)
    x.append(x1)
    z.append(x1)
    xB = 0
    if(x1 > x2):
        w = x1+1
        for j in range(0,len(y)-2):
            if slope > 1:
                xB = z[j] - (1/slope)
                print(xB)
            else:
                xB = z[j] - slope
                print(xB)
            z.append(xB)
            x.append(round(xB))
        x.append(x2)
        print(x)
    else:
        w = x2+1
        for j in range(0,len(y)-2):
            if slope > 1:
                xB = z[j] + (1/slope)
                print(xB)
            else:
                xB = z[j] + slope
                print(xB)
            z.append(xB)
            x.append(round(xB))
        x.append(x2)
        print(x)
    
#MATRIX = [[[0,0,0,0] for X in range(w)] for Y in range(h)]
print("#######################")
print(x)
print(y)
#X = zip(x,y)
#for a,b in X:
  #  MATRIX[abs(w-a)][abs(h-b)] = [0,0,0,255]  
#for i in MATRIX:
 #   print(i)
#MATRIX = np.array(MATRIX)
#img = Image.fromarray(MATRIX.astype('uint8'),'RGBA')
#plt.imshow(img)
#plt.show()

