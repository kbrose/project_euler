#include <stdio.h>

int f_digs(int n, int *f)
{
  int s = 0;
  while (n > 0){
    s += f[n % 10];
    n /= 10;
  }
  return s;
}

int in(int n, int *arr, int len)
{
  int i;
  for(i = 0; i < len; i++){
    if (n == arr[i])
      return 1;
  }
  return 0;
}

int main()
{
  int f[10] = {1,1,2,6,24,120,720,5040,40320,362880};
  int non_repeats;
  int arr[65];
  int i, n, counter;
  int temp_n;
  counter = 0;
  for(n = 2; n < 1000000; n++){
    temp_n = n;
    non_repeats = 0;
    for(i = 0; i < 65; i++){
      arr[i] = -1;
    }
    while (!in(temp_n,arr,65)){
      arr[non_repeats++] = temp_n;
      temp_n = f_digs(temp_n,f);
      if (non_repeats > 60){
	non_repeats = 0;
	break;
      }
    }
    if (non_repeats == 60)
      counter++;
  }
  printf("counter: %d\n", counter);
  
  return 0;
}
