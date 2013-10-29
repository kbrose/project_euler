#include <stdio.h>

int main()
{
  int counter = 0;
  int is3 = 3;
  int i = 0;
  
  for(i = 0; i < 1000; i+=5){
    if(is3 == 3){
      is3 = 1;
      continue;
    }
    counter += i;
    is3++;
  }

  for(i = 0; i < 1000; i+=3){
    counter += i;
  }

  printf("sum: %d\n", counter);

  return 0;
}
