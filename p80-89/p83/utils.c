#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#include "utils.h"

/* Kevin Rose, kbrose */
/* CS 152 Winter 2012 */
/* hw7 */

char *string_init(int sz)
{
  int i;
  char *new = (char*)malloc(sz*sizeof(char));
  if (new==NULL) {
    fprintf(stderr,"string_init: malloc failure\n");
    exit(1);
  }
  for(i=0; i<sz; i++)
    new[i] = '\0';
  return new;
}

char *trim(char *s)
{
  int i;
  int n = strlen(s);
  int first_non_space=0, last_non_space=n-1;
  char buf[n+1];
  for (i=0; i<n+1; i++)
    buf[i] = '\0';
  while (first_non_space<n && isspace(s[first_non_space]))
    first_non_space++;
  while (last_non_space>0 && isspace(s[last_non_space]))
    last_non_space--;
  for (i=first_non_space; i<=last_non_space; i++)
    buf[i-first_non_space] = s[i];
  return strdup(buf);
}
