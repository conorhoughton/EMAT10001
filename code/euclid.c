#include <stdio.h>
#include <math.h>

int euclid(int x,int y)
{
  if(y==0)
    return x;

  return euclid(y,x%y);

}

int main()
{

  int x=17*3;
  int y=17*4;

  int gcd=euclid(x,y);

  printf("gcd=%i\n",gcd);
}
