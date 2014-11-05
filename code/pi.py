import math

total=0
n=1
mp=1
pi=4*math.atan(1)

while n<10000:
    total+=mp*4.0/n
    mp=-mp
    n+=2
    print pi,
    print total,
    print math.fabs(total-pi)
