#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dj.h"
#include "linked-list.h"
#include "hash-table.h"
#include "vert-edge.h"

/* Kevin Rose, kbrose */
/* CS 152 Winter 2012 */
/* lab 8 */

unsigned long hash(char *s)
{
  unsigned long res = 17;
  while(*s != '\0'){
    res = (res * 37) + *s; 
    s++;
  }
  return res;
}

/* htbl_init : int -> htbl* */
/* allocate space for a new hash table of given size */
/* all buckets must initially contain the empty list */
htbl *htbl_init(int sz)
{
  htbl *hash_tab;
  hash_tab = (htbl *)malloc(sizeof(htbl));
  
  hash_tab->buckets = (sll **)malloc(sizeof(sll *) * sz);
  hash_tab->n_buckets = sz;
  while(sz > 0){
    hash_tab->buckets[sz] = NULL;
    sz--;
  }
  return hash_tab;
}

/* htbl_add : (htbl*, char*) -> int */ 
/* add string s to hast table t */
/* return the number of strings in s's bucket _after_ inserting it */
int htbl_add(htbl *t, char *name, int done, int dist, char *pred, char *edge, int i)
{
  unsigned long h = hash(name);
  h = h % (t->n_buckets);
  sll *bucket = t->buckets[h];
  t->buckets[h] = sll_cons(name, done, dist, pred, edge, i, t->buckets[h]);
  return sll_length(bucket);
}

/* htbl_member : (htbl*, char*) -> int */
/* test membership of given string in given table */
/* the integer returned is a (pseudo) boolean */
int htbl_member(htbl *t, char *s)
{
  unsigned long h = hash(s);
  return(sll_member(t->buckets[h % (t->n_buckets)], s));
}

/* htbl_show : htbl* -> <void> */
/* print a represntation of the hash table to stdout */
/* USED WHILE TESTING, NOT IN FINAL PROGRAM */
void htbl_show(htbl *t)
{
  int n = 0;
  while(n < t->n_buckets){
    printf("[%d]\t", n);
    sll_show(t->buckets[n]);
    printf("\n");
    n++;
  }
}

/* htbl_find : (htbl*, char*) -> int */
/* finds a vertex name, returns its corresponding array index */
/* return -1 if not found */
int htbl_find(htbl *t, char* vertex)
{
  unsigned long h = hash(vertex);
  return(sll_find(t->buckets[h%(t->n_buckets)], vertex));
}

/* frees a hash table */
void htbl_free(htbl *t)
{
  int i;
  for(i = 0; i < t->n_buckets; i++){
    sll_free(t->buckets[i]);
  }
  free(t);
}
