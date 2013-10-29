#include <stdio.h>

int fact(int x)
{
  int fact = 1;
  while(x > 0){
    fact *= x;
    x--;
  }
  return fact;
}

int main()
{
  int i, j, k;
  int arr[11];
  int sum = 0;
  for(i = 0; i < 11; i++)
    arr[i] = i;

  for(i = 9; i > -1; i--){
    j = 0;
    while(j < 10){
      if(sum + (fact(i)*j) > 999999){ 
	/* apparently 0123456789 is the first, not the zeroeth, permutation */
	j--;
	break;
      }
      j++;
    }
    sum += fact(i)*j;
    printf("%d", arr[j]);
    for(; j < 10; j++)
      arr[j] = arr[j+1];
  }
  printf("\n");

  return 0;
}
