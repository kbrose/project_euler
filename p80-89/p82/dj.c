/* dj.c */

/* Kevin Rose, kbrose */
/* CS 152 Winter 2012 */
/* hw7 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//#include "dj.h"
//#include "structs.h"
#include "linked-list.h"
#include "hash-table.h"
#include "vert-edge.h"
#include "parse.h"
#include "utils.h"
#include "commands.h"
#include "dj.h"

dj_table new_dj_table(char *name, int done, int dist, char *pred, char *edge)
{
  dj_table new = (dj_table)malloc(sizeof(struct dj_table));

  new->name = name;
  new->done = done;
  new->dist = dist;
  new->pred = pred;
  new->edge = edge;

  return new;
}

sll *dj_path(char *source, char *target, htbl *t, 
	     edge_cost *adj_mat, dj_table *dj_arr, int size)
{
  int i = htbl_find(t, source);
  int j = htbl_find(t, target);
  int n, past_i;
  int curr_dist, edge_dist;
  sll *path = NULL;


  if(i == -1 || j == -1){ /* if source or target not in graph */
    printf("   -error: unrecognized vertex name(s) given\n");
    printf("   -try typing \"s -v\" for a list of current vertices\n");
    return NULL;
  }

  /* initializes the dj_table */
  for(j = 0; j < size; j++){
    dj_arr[j]->done = 0;
    dj_arr[j]->dist = INF;
    dj_arr[j]->pred = NULL;
    dj_arr[j]->edge = NULL;
  }
  dj_arr[i]->dist = 0;

  /* maybe have a check to make sure source and target are in it */
  j = htbl_find(t, target);


  while(strcmp(dj_arr[i]->name, target)){
    past_i = i;
    dj_arr[i]->done = 1;
    curr_dist = dj_arr[i]->dist;
    for(j = 0; j < size; j++){
      n = (i * size) + j;
      if(adj_mat[n] != NULL){
	edge_dist = adj_mat[n]->cost;
	if(dj_arr[j]->dist > curr_dist + edge_dist ||
	   dj_arr[j]->dist == INF){
	  dj_arr[j]->dist = curr_dist + edge_dist;
	  dj_arr[j]->pred = dj_arr[i]->name;
	  dj_arr[j]->edge = adj_mat[n]->edge;
	}
      }
    }
    for(j = 0; j < size; j++){
      if(!dj_arr[j]->done && dj_arr[j]->dist != INF){
	i = j; /*sets j to be the first not-done vertex that has been reached*/
	break;
      }
    }
    if(past_i == i){/* all vertices are done, no path found */
      printf("These vertices are not connected\n");
      return NULL;  /* return NULL to indicate error in finding */
    }
    for(j = 0; j < size; j++){
      if(dj_arr[j]->dist < dj_arr[i]->dist && 
	 !dj_arr[j]->done &&
	 dj_arr[j]->dist != INF)
	i = j;
    }
  }
  /* recursively go down preds */
  while(strcmp(dj_arr[i]->name, source)){
    path = sll_cons(dj_arr[i]->name,
		    dj_arr[i]->done,
		    dj_arr[i]->dist,
		    dj_arr[i]->pred,
		    dj_arr[i]->edge,
		    i, path);
    i = htbl_find(t, dj_arr[i]->pred);
  }
  path = sll_cons(dj_arr[i]->name,
		  dj_arr[i]->done,
		  dj_arr[i]->dist,
		  dj_arr[i]->pred,
		  dj_arr[i]->edge,
		  i, path);
  return path;
}


/*
void show_connected(edge_cost *adj_mat, dj_table *dj_arr, int size)
{
  int j;
  int k;

  printf("connected?\n");

  for(j = 0; j < size; j++){
    for(k = 0; k < size; k++){
      if(j == k) /* self connection 
	continue;
      printf("   %s -> %s: ", dj_arr[j]->name, dj_arr[k]->name);
      if(adj_mat[(j * size) + k] != NULL){
	printf("yes! ");
	printf("(%s, %d)\n", 
	       adj_mat[(j * size) + k]->edge, 
	       adj_mat[(j * size) + k]->cost);
      } else {
	printf("no\n");
      }
    }
  }
  return;
}


/* USED TO TEST dj.c FUNCTIONS */
/*
int main()
{
  dj_table d;
  d = new_dj_table("A", 0, -1, NULL, NULL, 5);

  printf("name: %s\n", d->name);
  printf("done: %d\n", d->done);
  printf("dist: %d\n", d->dist);
  printf("pred: %s\n", d->pred);
  printf("edge: %s\n", d->edge);
  printf("i   : %d\n", d->i);

  return 0;
}
*/
