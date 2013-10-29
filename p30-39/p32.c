#include <stdio.h>

void reset(int arr[10])
{
  int i;
  arr[0] = 1;
  for(i = 1; i < 11; i++)
    arr[i] = 0;

  return;
}

int ispan(int a, int b, int c)
{
  int i;
  int pan[10];
  reset(pan);

  while(a != 0){
    if(pan[a % 10])
      return 0;
    pan[a % 10] = 1;
    a /= 10;
  }

  while(b != 0){
    if(pan[b % 10])
      return 0;
    pan[b % 10] = 1;
    b /= 10;
  }

  while(c != 0){
    if(pan[c % 10])
      return 0;
    pan[c % 10] = 1;
    c /= 10;
  }

  for(i = 0; i < 11; i++)
    if(!pan[i])
      return 0;

  return 1;
}

int main()
{
  int i, n;
  int sum = 0;
  int arr[10000];
  for(i = 0; i < 10000; i++)
    arr[i] = 1;
  
  for(n = 1000; n < 10000; n++){
    for(i = 1; i < n/2; i++){
      if(!(n % i)){
	if(ispan(i, n/i, n)){
	  if(arr[n]){
	    sum += n;
	    arr[n] = 0;
	  }
	}
      }
    }
  }

  printf("%d\n", sum);

  return 0;
}
