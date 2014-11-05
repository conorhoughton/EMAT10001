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


  
  vector<int> c_ms;

  /*
  //PH example
  
  int p=10007;
  int d=8005;

  c_ms.push_back(1122);
  c_ms.push_back(6853);
  c_ms.push_back(3947);
  c_ms.push_back(8606);
  */


  //RSA example
  int p=10001;
  int d=3917;
  c_ms.push_back(7427);
  c_ms.push_back(2001);
  c_ms.push_back(1929);
  c_ms.push_back(672);


  


  for(unsigned int j=0;j<c_ms.size() ;++j)
    {
      
      int c_m=c_ms[j];

      cout<<c_m<<"^{"<<d<<"}&\\equiv "<<power(c_m,d,p)<<" \\pmod{"<<p<<"}\\cr"<<endl;
    }


}
