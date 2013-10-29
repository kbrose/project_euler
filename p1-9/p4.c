#include <stdio.h>
#include <math.h>

int reverse(int n)
{
  int log10 = 1;
  int work_n = n;
  int res = 0;

  while(work_n > 9){
    work_n /= 10;
    log10 *= 10;
  }

  while(log10 > 1){
    res += (n % 10) * log10;
    n /= 10;
    log10 /= 10;
  }

  return res + n;
}

int main()
{
  int a;
  int b;
  int curr = 0;

  for(a = 100; a < 1000; a++)
    for(b = 100; b < 1000; b++)
      if((a * b == reverse(a * b)) && (a * b) > curr)
	curr = a * b;

  printf("%d\n", curr);
  
  return 0;
}
