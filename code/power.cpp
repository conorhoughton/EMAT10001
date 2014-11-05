/*
In exercise sheet 4 there is a description of a program to efficiently
calculate a^b (mod p), however, since the numbers in lecture6 are not
particularly large a simpler approach is used here for so it easier to
convince yourself that it does what I claim it does, the loop
multiplies by c_m each time it goes around the loop d=8005 times, the
modulus with p=10007 so a never becomes too large.

The output is designed to give latex for copying directly in to the notes.
*/


#include<cstdlib>
#include<iostream>
#include<vector>

using namespace std;

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

      int a=1;

      for(unsigned int i=0;i<d ;++i)
	{
	  a*=c_m;
	  a=a%p;
	}
      
      cout<<c_m<<"^{"<<d<<"}&\\equiv "<<a<<" \\pmod{"<<p<<"}\\cr"<<endl;
    }
}
