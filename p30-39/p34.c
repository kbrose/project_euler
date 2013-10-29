#include <stdio.h>

int sum_digs_fact(int n)
{
  int arr[10] = {1,1,2,6,24,120,720,5040,40320,362880};
  int sum = 0;
  
  while(n > 0){
    sum += arr[n % 10];
    n /= 10;
  }

  return sum;
}

int main()
{
  int i;
  int sum = 0;

  for(i = 3; i < 2500000; i++)
    if(i == sum_digs_fact(i))
      sum += i;

  printf("%d\n", sum);

  return 0;
}
