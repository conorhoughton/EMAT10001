
import random

limit_a_b=20
limit_c=10

trials=20

score=0

i=0


seed=input("\nInput an integer to seed the random number generator: ");
random.seed(seed);

print "\n"

while i<trials:
    a=random.randrange(limit_a_b-1)+1
    b=random.randrange(limit_a_b-1)+1
    c=random.randrange(limit_c-2)+2
    r=input(str(i+1)+" What is "+str(a)+"X"+str(b)+" mod "+str(c)+" ")
    if(r==(a*b)%c):
        print "Well done\n"
        score+=1
    else:
        print "No it is "+str((a*b)%c)+"\n"
    i+=1

print "You got "+str(score)+" out of "+str(trials)+"\n"
