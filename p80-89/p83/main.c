/* main.c */

/* Kevin Rose, kbrose */
/* CS 152 Winter 2012 */
/* hw7 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#include "structs.h"
#include "dj.h"
#include "linked-list.h"
#include "hash-table.h"
#include "vert-edge.h"
#include "parse.h"
#include "utils.h"
#include "commands.h"

#define MAX_CMD 512

void greet()
{
  printf("***************************************************************\n");
  printf("Welcome to dj, a Dijkstra's algorithm shortest path calculator.\n");
  printf("Designed and built by Kevin Rose, March 2012.\n");
  printf("Type \"help\" or \"?\" for instructions.\n");
  printf("Type \"exit\" to exit.\n");
}

void prompt()
{
  printf("]> ");
  fflush(stdout);
  return;
}

/* return when user indicates exit */
void interact()
{
  int i;
  char buf[MAX_CMD];
  char *cmd;
  while (1) {
    prompt();
    /* read command */
    for (i=0; i<MAX_CMD; i++)
      buf[i] = '\0';   
    fgets(buf,MAX_CMD,stdin);
    cmd = trim(buf);
    /* process command */
    /* (returns true when cmd indicates exit) */
    if (process_command(cmd))
      return;
  }
}

int main(int argc, char *argv[])
{
  greet();
  interact();
  /* When interact returns, session is done. */
  printf("Bye!\n");
  return 0;
}
