#include <stdio.h>
#include <math.h>

int main()
{
  double i, root, j;
  int canbe[28200];
  double abun[28200];
  int counter = 0;
  double sum;
  for(i = 0; i < 28200; i++){
    canbe[(int)i] = 0;
    abun[(int)i] = 0;
  }

  for(i = 10; i < 28124; i++){
    root = sqrt(i);
    sum = 1;
    for(j = 2; j < (int)(root+1); j++){
      if(!((long int)i % (long int)j)){
	sum += j;
	if(i / j != j)
	  sum += i / j;
      }
    }
    if(i < sum){
      abun[counter++] = i;
      printf("%d\n", (int) i);
    }
  }

  for(i = 0; i < 28200; i++){
    for(j = i; j < 28200; j++){
      if(abun[(int)i] && abun[(int)j])
	counter = abun[(int)i] + abun[(int)j];
      if(counter < 28150){
	canbe[counter] = 1;
	
	//printf("%d+%d = %d\n", (int)abun[(int)i], (int)abun[(int)j], counter);
      }
    }
  }

  sum = 0;
  for(i = 0; i < 28124; i++)
    if(!canbe[(int)i]){
      sum += i;
      //printf("%d ", (int)i);
    }

  printf("\n%lf\n", abun[0]);

  printf("sum: %lf\n", sum);

  return 0;
}
