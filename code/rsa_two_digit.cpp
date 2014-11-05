#include<cstdlib>
#include<cmath>
#include<iostream>
#include<string>
#include<vector>

using namespace std;

vector<int> number(string text)
{
  vector<int> text_numbers;

  for(unsigned int i=0;i<text.length() ;++i)
    text_numbers.push_back(int(text[i])-97);

  return text_numbers;
}

string text(vector<int> numbers)
{
  string number_text;

  for(unsigned int i=0;i<numbers.size(); ++i)
    number_text.push_back(char(numbers[i]+97));

  return number_text;
}
  
int encode(int number,int n, int e)
{
  return int(pow(number,e))%n;
}


int main()
{
  string source_text="blamecanada";
  int n=111;
  int e=5;

  vector<int> text_numbers=number(source_text);

  for(unsigned int i=0;i<text_numbers.size() ;++i)
    text_numbers[i]=encode(text_numbers[i],n,e);

  for(unsigned int i=0;i<text_numbers.size() ;++i)
    cout<<text_numbers[i]<<endl;
}
