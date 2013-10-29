#include <stdio.h>

int check(int *primes, int n, int i)
{
  int it;

  for(it = 0; it < n; it++)
    if(!(i % primes[it]))
      return 0;
  return 1;
}

int main()
{
  int primes[200000];
  int n = 1;
  int i;
  long int sum = 0;
  primes[0] = 2;

  for(i = 3; i < 2000000; i++)
    if(check(primes, n, i)){
      primes[n] = i;
      n++;
    }

  for(i = 0; i < n; i++)
    sum += primes[i];

  printf("n: %d\n", n);
  printf("primes[0]: %d\nprimes[1]: %d\nprimes[99]: %d\nprimes[148932]: %d\n", primes[0], primes[1], primes[99], primes[148932]);
  printf("sum: %ld\n", sum);
      
  return 0;
}
