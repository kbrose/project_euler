#include <stdio.h>
#include <math.h>

int main()
{
  double i1, i2;
  double tri = 1;
  int counter = 0;
  double root;
  i1 = 2;
  
  while(counter < 500){
    counter = 0;
    tri += i1;
    root = sqrt(tri);
    for(i2 = 1; i2 < root; i2++){
      if(!((long int)tri % (long int)i2))
	counter++;
    }
    counter *= 2;
    i1++;
  }
  
  printf("tri: %lf\n", tri);

  return 0;
}
