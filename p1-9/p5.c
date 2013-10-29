#include <stdio.h>

int main()
{
  int n = 2520;
  int i;
  int works = 0;

  while(1){
    works = 1;
    for(i = 2; i < 21; i++)
      if(n % i)
	works = 0;
    if(works)
      break;
    n++;
  }

  printf("%d\n", n);

  return 0;
}
