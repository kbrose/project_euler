#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dj.h"
#include "linked-list.h"
#include "hash-table.h"
#include "vert-edge.h"
#include "parse.h"

/* Kevin Rose, kbrose */
/* CS 152 Winter 2012 */
/* lab 8 */

/* converts a string linked list to an array of exact size */
/* then frees the string linked list */
dj_table *sll_to_djtab_arr(sll *dj_sll, int size)
{
  int i;
  int n;
  dj_table *new_dj_arr = (dj_table *)malloc(sizeof(dj_table) * size);

  for(i = 0; i < size; i++){
    n = dj_sll->i-1;
    new_dj_arr[n] = new_dj_table(dj_sll->dj->name,
				 dj_sll->dj->done,
				 dj_sll->dj->dist,
				 dj_sll->dj->pred,
				 dj_sll->dj->edge);
    dj_sll = dj_sll->next;
  }

  sll_free(dj_sll);
  return new_dj_arr;
}

/* returns the sll containing all the vertices
 * as a side effect places number of vertices into sll->nn->n 
 * and places vertices into hash table */
sll *parse_vertices(htbl *t, FILE *f)
{
  char c;
  int i = 0;
  int i2 = 0;
  char name[500]; /* expects vertex name no longer than 500 chars */
  sll *vert_sll = NULL;
  
  while((c = fgetc(f)) != '#' && c != EOF){
    i2 = 0;
    name[i2++] = c;
    while((c = fgetc(f)) != '\n')
      name[i2++] = c;
    name[i2] = '\0';
               /* initializes the dj_table to what it should be */
    vert_sll = sll_cons(strdup(name),0,INF,NULL,NULL,i+1,vert_sll);
                                          /*i+1 = current length of list*/
    htbl_add(t, strdup(name), 0, INF, NULL, NULL, i);
    i++;
  }
  return vert_sll;
}

void parse_edges(edge_cost *adj_mat, htbl *t, int size, FILE *f)
{
  char c;
  char vert_name1[500];
  char vert_name2[500];
  char edge_name[500];
  int cost;
  int i, i2;
  int j, k;
  int left_arrow; /* 1 if left arrow present */
  int right_arrow; /* similar */

  while((c = fgetc(f)) != EOF){
    left_arrow = 0;
    right_arrow = 0;
    i2 = 0;
    vert_name1[i2++] = c;
    while((c = fgetc(f)) != '<' && c != '=')
      vert_name1[i2++] = c;
    vert_name1[i2] = '\0';
    i2 = 0;
    
    if(c == '<'){
      left_arrow = 1;
      c = fgetc(f);
    }
    if(c == '=')
      c = fgetc(f);
    if(c == '>'){
      right_arrow = 1;
      c = fgetc(f);
    }

    vert_name2[i2++] = c;
    while((c = fgetc(f)) != ',')
      vert_name2[i2++] = c;
    vert_name2[i2++] = '\0';
    i2 = 0;

    while((c = fgetc(f)) != ','){
      edge_name[i2++] = c;
    }
    edge_name[i2] = '\0';

    fscanf(f, "%d", &cost);

    if(left_arrow){
      k = htbl_find(t, vert_name1);
      j = htbl_find(t, vert_name2);
      adj_mat[(j * size) + k] = new_edge_cost(edge_name, cost);
    }
    if(right_arrow){
      j = htbl_find(t, vert_name1);
      k = htbl_find(t, vert_name2);
      adj_mat[(j * size) + k] = new_edge_cost(edge_name, cost);
    }
    fscanf(f, "\n");
  }
}

