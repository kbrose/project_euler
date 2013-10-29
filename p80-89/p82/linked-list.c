#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dj.h"
#include "vert-edge.h"
#include "linked-list.h"
#include "hash-table.h"

/* Kevin Rose, kbrose */
/* CS 152 Winter 2012 */
/* lab 8 */

/* sll_cons : (char*, sll*) -> sll* */
/* build new list with given string at the head */
sll *sll_cons(char *name, int done, int dist, char *pred, char *edge, int i, sll *ss)
{
  sll *string_list = (sll *)malloc(sizeof(sll));
  dj_table d = new_dj_table(name, done, dist, pred, edge);
  string_list->dj = d;
  string_list->i = i;
  string_list->next = ss;
  return string_list;
}

/* sll_length : sll* -> int */
/* return the number of strings in the given list */
int sll_length(sll *ss)
{
  int n = 0;
  while(ss != NULL){
    n++;
    ss = ss->next;
  }
  return n;
}

/* sll_member : (sll*, char*) -> int */
/* test membership of given string in given list */
/* use strcmp to compare strings */
int sll_member(sll *ss, char *s)
{
  while(ss != NULL){
    if(!strcmp(s, ss->dj->name)){
      return 1;
    }
    ss = ss->next;
  }
  return 0;
}

/* sll_show : sll* -> <void> */
/* print a representation of the linked list to stdout */
/* USED WHILE TESTING, NOT IN FINAL PROGRAM */
int sll_show(sll *ss)
{
  int curr_dist;
  if(ss == NULL){
    /*printf("you are at your destination\n");*/
    return;
  }
  /*printf("From %s, ", ss->dj->name);*/
  curr_dist = ss->dj->dist;
  ss = ss->next;
  while(ss != NULL){
    /*printf("go along \"%s\" (cost: %d) to \"%s\".\nFrom \"%s\", ", 
	   ss->dj->edge, ss->dj->dist - curr_dist, 
	   ss->dj->name, ss->dj->name);*/
    curr_dist = ss->dj->dist;
    ss = ss->next;
  }
  /*printf("go nowhere because you have arrived!\n");*/
    /*printf("The total cost was %d.\n", curr_dist);*/
  return curr_dist;
}

/* returns the corresponding array index */
/* returns -1 if not found */
int sll_find(sll *ss, char *vertex)
{
  while(ss != NULL){
    if(!strcmp(vertex, ss->dj->name)){
      return ss->i;
    }
    ss = ss->next;
  }
  return -1;
}

/* frees all the elements of a sll */
void sll_free(sll *ss)
{
  if(ss == NULL){
    return;
  } else {
    sll_free(ss->next);
    free(ss->next);
  }
}
