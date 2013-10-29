#ifndef _LINKED_LIST_H
#define _LINKED_LIST_H

/* linked lists of strings */

#include "dj.h"

struct string_list_node {
  dj_table dj;
  int i;
  struct string_list_node *next;
};

typedef struct string_list_node sll; /* "sll" for "string linked list" */

/* By convention, the empty list is NULL. */

/* sll_cons : (char*, sll*) -> sll* */
/* build new list with given string at the head */
sll *sll_cons(char *name, int done, int dist, char *pred, char *edge, int i, sll *ss);

/* sll_length : sll* -> int */
/* return the number of strings in the given list */
int sll_length(sll *ss);

/* sll_member : (sll*, char*) -> int */
/* test membership of given string in given list */
/* use strcmp to compare strings */
int sll_member(sll *ss, char *s);

/* sll_show : sll* -> <void> */
/* print a representation of the linked list to stdout */
void sll_show(sll *ss);

/* returns the corresponding array index */
/* returns -1 if not found */
int sll_find(sll *ss, char *vertex);

/* frees all the elements of a sll */
void sll_free(sll *ss);

#endif /* _LINKED_LIST_H */
