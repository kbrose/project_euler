/* main.h */

/* declares all the global variables */
#ifndef _MAIN_H
#define _MAIN_H

#define MAX_CMD 512

FILE *f;
char *curr_file = NULL;
dj_table *dj_arr = NULL;
htbl *t;
edge_cost *adj_mat = NULL;
char source[MAX_CMD];
char target[MAX_CMD];
int size;

#endif
