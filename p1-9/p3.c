#include <stdio.h>

long int recurse(long int p, long int n)
{
  long int prev = p;

  while((n % p) && (p < 775147)){
    p += 2;
  }

  if(p > 775146)
    return prev;

  return recurse(p, n / p);
}

int main()
{
  long int n = 600851475143;

  printf("%ld\n", recurse(3, n));

  return 0;
}
