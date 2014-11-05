#include<cstdlib>
#include<iostream>
#include<cmath>

using namespace std;

int main()
{

  int n=1000;

  int max_divisors=0;
  int max_divisors_i=0;

  for(unsigned int i=1;i<n+1 ;++i)
    {
      int divisors=2;
      for(unsigned int j=2;j<i ;++j)
	if(i%j==0)
	  divisors++;
      //      cout<<i<<" "<<divisors<<endl;
      if(divisors>max_divisors)
	{
	  max_divisors=divisors;
	  max_divisors_i=i;
	}
    }
  
  cout<<max_divisors<<" "<<max_divisors_i<<endl;

}
