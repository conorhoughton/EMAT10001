/*
This is a more efficient version of the power.cpp program, if we want

a^r (mod p)

we write r as r_0+2r_1+4r_2+ . . .

where all the r_i's are zero or one. We can work out 

a^{2^n} (mod p)

by successively squaring.

*/


#include<cstdlib>
#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

int power(int total,int a,int n,int p)
{

  if(n%2==1)
    {
      total*=a;
      total=total%p;
      n-=1;
    }

  a=(a*a)%p;

  if(n==0)
    return total;

  return power(total,a,n/2,p);
   
}


int power(int a,int n,int p)
{
  return power(1,a,n,p);
}



int main()
{



  int n=pow(8,9);
  
  cout<<power(7,n,100)<<endl;

}
