#include <stdio.h>

int main()
{
  double a, b, c, d;
  double fracn, fracd, sumn, sumd;
  sumn = sumd = 1;

  for(a = 1; a < 10; a++){
    for(b = 1; b < 10; b++){
      for(c = 1; c < (a + 1); c++){
	for(d = 1; d < 10; d++){
	  fracd = (a*10) + b;
	  fracn = (c*10) + d;
	  if(fracd <= fracn)
	    break;
	  if(a == c)
	    if(fracn/fracd == d/b){
	      sumn *= b;
	      sumd *= d;
	    }
	  if(a == d)
	    if(fracn/fracd == c/b){
	      sumn *= b;
	      sumd *= c;
	    }
	  if(b == c)
	    if(fracn/fracd == d/a){
	      sumn *= a;
	      sumd *= d;
	    }
	  if(b == d)
	    if(fracn/fracd == c/a){
	      sumn *= a;
	      sumd *= c;
	    }
	}
      }
    }
  }

  printf("%d / %d\n", (int)sumd, (int)sumn);


  return 0;
}
