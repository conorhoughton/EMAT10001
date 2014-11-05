/*
  This is a slightly more robust version of euclid_linear.c, the
  pointers are initialized inside the calling function not in the main.
 */


#include <stdio.h>
#include <math.h>

struct GCD_Numbers
{
  int gcd;
  int m;
  int n;
};

struct GCD_Numbers euclid(int x,int y)
{
  if(x<y)
    {
      int temp=x;
      x=y;
      y=temp;
    }



  int m_var=1;
  int n_var=0;

  int *m=&m_var;
  int *n=&n_var;

  int gcd_value=euclid_r(x,y,m,n);

  struct GCD_Numbers gcd_numbers;
  gcd_numbers.gcd=gcd_value;
  gcd_numbers.m=*m;
  gcd_numbers.n=*n;

  return gcd_numbers;

}

int euclid_r(int x,int y,int * m, int * n)
{
  if(y==0)
      return x;

  int k=x/y;
  int r=x%y;

  int gcd=euclid_r(y,x%y,m,n);

  int temp=*m;
  *m=*n;
  *n=-(*n)*k+temp;
  
  return gcd;

}

int main()
{

  int x=11*17;
  int y=5*17;

  struct GCD_Numbers gcd_numbers=euclid(x,y);

  printf("%i=(%i)*%i+(%i)*%i\n",gcd_numbers.gcd,gcd_numbers.m,x,gcd_numbers.n,y);
}
