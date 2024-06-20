import math 
import numpy as np

def expMethod1() :  # Using the Calculus limit definition to approximate e --> comes from Compound interest
    getAcc = input("How accurate do you want your Euler's Number to be? Very accurate, not         accurate or Engineer's Approximation? ")

    veryAcc = 1000000     # Degrees of accuracy
    notAcc = 1000
    engineersAcc = 2  # Engineers are silly! - If an engineer reads this, I'm not sorry...

    if getAcc == "Very accurate":
        print(((1+(1/veryAcc))**veryAcc))

    if getAcc == "Not accurate":
        print(((1+(1/notAcc))**notAcc))

    if getAcc == "Engineer's Approximation":
        print(engineersAcc)


def expMethod2() :               # Series definition of Euler's Number - derived from Maclaurin (taylor polynomial centred at 0) expansion of e^x when x = 1
    n = int(input("Choose a positive integer: "))

    eulerNum = 0

    for i in range(0, n):
        eulerNum = eulerNum + 1/math.factorial(i)

    print(eulerNum)

#def expMethod3() : 
