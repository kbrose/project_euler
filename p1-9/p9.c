#include <stdio.h>

int main()
{
  int a, b, c;

  for(a = 1; a < 1000; a++)
    for(b = 2; b < 1000; b++)
      for(c = 3; c < 1000; c++)
	if((a*a + b*b == c*c) && (a + b + c == 1000)){
	  printf("%d\n", a*b*c);
	  return 0;
	}

  return 0;
}
