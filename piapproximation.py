from numpy import random                       # Monte Carlo Method - Approximation of Pi
import numpy as np 
import matplotlib.pyplot as plt

N = 1000000000000

circleX = []
circleY = []

squareX = []
squareY = []

i = 1

while i <= N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    if (x**2 + y**2 <= 1):               # Coordinates which are inside circle are added to component lists.
        circleX.append(x)                # Otherwise, in the square coordinate component lists.
        circleY.append(y)
    else:
        squareX.append(x)
        squareY.append(y)
    i += 1

piApprox = 4*len(circleX)/float(N)      # Algebraic manipulation of circle area formula, and square area, will lead you to this (but with pseudorandom points)

print(f"Pi is approximately: {piApprox}")
print(f"Pi is: {np.pi}")

plt.plot(circleX,circleY,'b.')
plt.plot(squareX,squareY,'r.')
plt.show()                                   n -> inf, value approaches pi.
