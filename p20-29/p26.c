#include <stdio.h>
#include <math.h>

long int MultOrd(long int a, long int n)
{
  long int k;

  if(n == 1)
    return 1;
  
  for(k = 1; ((long int)pow(a,k) % n) != 1; k++)
    ;

  return k;
}

int main()
{
  long int i, j, currlen, currid, templen;
  currlen = 0;
  currid = 0;

  for(i = 3; i < 1000; i++){
    j = i;
    while(!(j % 5))
      j /= 5;
    while(!(j % 2))
      j /= 2;
    //printf("%d\t%d\n", i, j);
    templen = MultOrd(10, j);
    if(templen > currlen){
      currlen = templen;
      currid = i;
      printf("%ld\t%ld\n", currlen, currid);
    }
  }

  printf("%ld\n", currid);
  printf("%ld\n", MultOrd(10, 989));

  return 0;
}
