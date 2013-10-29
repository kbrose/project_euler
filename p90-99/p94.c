#include <stdio.h>

int main()
{
  unsigned long int curr_square, curr_sqrt, a, b, two_a, test1, test2, sum;
  int num_of_times = 0;
  curr_square = 0;
  curr_sqrt = 0;
  sum = 0;

  for (a = 0; a < 333333334; a++){
    two_a = a << 1;
    test1 = (3 * a * a) - two_a - 1;
    test2 = test1 + (two_a << 1);
    if (curr_square < test1){
      curr_sqrt++;
      curr_square = curr_sqrt * curr_sqrt;
    }
    if (curr_square == test1){
      sum += (a << 1) + a + 1;
      num_of_times++;
    }

    if (curr_square < test2){
      curr_sqrt++;
      curr_square = curr_sqrt * curr_sqrt;
    }
    if (curr_square == test2){
      if (a != 1){
	sum += (a << 1) + a - 1;
      }
      num_of_times++;
    }
  }
  printf("sum: %lu\n", sum);
  printf("number of triangles: %d\n", num_of_times);
}
