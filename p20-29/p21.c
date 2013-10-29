#include <stdio.h>
#include <math.h>

int main()
{
  int AmiSum = 0;
  int firstSum, secondSum;
  int i, j;

  for(i = 1; i < 10000; i++){
    firstSum = 0;
    secondSum = 0;
    for(j = 1; j < (i / 2)+1; j++)
      if(!(i % j))
	firstSum += j;
    for(j = 1; j < (firstSum / 2)+1; j++)
      if(!(firstSum % j))
	secondSum += j;
    if(secondSum == i){
      if(secondSum == firstSum)
	continue;
      AmiSum += i;
      printf("i: %d\n", i);
      printf("\tf: %d\ts: %d\n", firstSum, secondSum);
    }
  }
   
  printf("%d\n", AmiSum);

  return 0;
}
