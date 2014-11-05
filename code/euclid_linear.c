/*
  This version recovers m and n, it passes them back through the
  recursion using pointers. It isn't very robust code, it initializes
  m and n in the main not in the function and it assumes x>y
*/


#include <stdio.h>
#include <math.h>

int euclid(int x,int y,int * m, int * n)
{
  if(y==0)
      return x;

  int k=x/y;
  int r=x%y;

  int gcd=euclid(y,x%y,m,n);

  int temp=*m;
  *m=*n;
  *n=-(*n)*k+temp;
  
  return gcd;

}

int main()
{

  int x=11*17;
  int y=5*17;

  int m_var=1;
  int n_var=0;

  int *m=&m_var;
  int *n=&n_var;


  int gcd=euclid(x,y,m,n);

  printf("%i=(%i)*%i+(%i)*%i\n",gcd,*m,x,*n,y);
}
