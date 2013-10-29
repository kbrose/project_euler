#include <stdio.h>

int main()
{
  int first = 1;
  int second = 2;
  int new = 3;
  int counter = 2;

  while(new < 4000000){
    if((new % 2))
      counter += new;
    first = second;
    second = new;
    new = first + second;
  }

  printf("sum: %d\n", counter);

  return 0;
}
