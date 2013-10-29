#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "linked-list.h"
#include "hash-table.h"
#include "vert-edge.h"

/* Kevin Rose, kbrose */
/* CS 152 Winter 2012 */
/* lab 8 */

edge_cost new_edge_cost(char *edge, int cost)
{
  edge_cost new = (edge_cost)malloc(sizeof(struct edge_cost));

  new->edge = strdup(edge); /* defensive copying */
  new->cost = cost;

  return new;
}

void show_connected(edge_cost *adj_mat, dj_table *dj_arr, int size)
{
  int j;
  int k;

  printf("connected?\n");

  for(j = 0; j < size; j++){
    for(k = 0; k < size; k++){
      if(j == k) /* self connection */
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

void show_neighbors(edge_cost *adj_mat, dj_table *dj_arr, int size)
{
  int i;
  int j;

  printf("neighbors:\n");
 
  for(i = 0; i < size; i++){
    printf("   %s:\n", dj_arr[i]->name);
    for(j = 0; j < size; j++){
      if(adj_mat[(i * size) + j] != NULL){
	printf("      %s\n", dj_arr[j]->name);
      }
    }
  }
  return;
}


void show_one_connection(edge_cost *adj_mat, dj_table *dj_arr, int size, int i)
{
  int j;
  printf("connections for %s:\n", dj_arr[i]->name);
  for(j = 0; j < size; j++){
    if(i == j) /* self connection */
      continue;
    printf("   %s -> %s: ", dj_arr[i]->name, dj_arr[j]->name);
    if(adj_mat[(i * size) + j] != NULL){
      printf("yes! ");
      printf("(%s, %d)\n", 
	     adj_mat[(i * size) + j]->edge, 
	     adj_mat[(i * size) + j]->cost);
    } else {
      printf("no\n");
    }
  }
}  
