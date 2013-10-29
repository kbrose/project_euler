#include <stdio.h>

int iscirc(int n, int primes[80000], int len)
{
  int rot, i, isprime;
  int log = 1;
  while(n >= log)
    log *= 10;
  log /= 10;
  rot = (n / 10) + ((n % 10)*log);
  while(n != rot){
    isprime = 0;
    for(i = 0; i < len && primes[i] <= rot; i++)
      if(primes[i] == rot)
	isprime = 1;
    if(!isprime)
      return 0;
    rot = (rot / 10) + ((rot % 10) * log);
  }

  return 1;
}

int main()
{
  int len = 1;
  int primes[80000];
  int i, j;
  int counter = 13;
  int isprime;

  primes[0] = 2;
  for(i = 3; i < 1000000; i++){
    isprime = 1;
    for(j = 0; j < len; j++){
      if(!(i % primes[j])){
	isprime = 0;
	break;
      }
    }
    if(isprime){
      primes[len++] = i;
    }
  }

  for(i = 100; i < 1000000; i++){
    isprime = 0;
    for(j = 0; j < len && primes[j] <= i; j++)
      if(primes[j] == i){
	isprime = 1;
	break;
      }
    if(isprime)
      if(iscirc(i, primes, len))
	counter++;
  }

  printf("%d\n", counter);

  return 0;
}
