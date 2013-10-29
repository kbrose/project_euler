#include <stdio.h>

int main()
{
  char c;
  while((c = getchar()) != EOF){
    if(c == ' ')
      c = '\n';
    putchar(c);
  }
  putchar(EOF);

  return 0;
}
