/* dj.h */

#ifndef _DJ_H
#define _DJ_H

#define INF -1

struct dj_table{
  char *name;
  int done;
  int dist;
  char *pred;
  char *edge;
};

typedef struct dj_table *dj_table;

dj_table new_dj_table(char *name, int done, int dist, char *pred, char *edge);
/*
sll *dj_path(char *source, char *target, htbl *t, 
	     edge_cost *adj_mat, dj_table *dj_arr, int size);
*/
#endif /* _DJ_H */
