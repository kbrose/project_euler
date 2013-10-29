commands.c
------------------
/* commands.c */

/* Kevin Rose, kbrose */
/* CS 152 Winter 2012 */
/* hw7 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "dj.h"
#include "linked-list.h"
#include "hash-table.h"
#include "vert-edge.h"
#include "parse.h"
#include "utils.h"
#include "commands.h"
#include "main.h"

void help()
{
  printf("==================== available commands ====================\n");
  printf("  ? (help)\n");
  printf("    provides information on available commands\n");
  printf("  r \"file_name\" (read)\n");
  printf("    reads file of name \"file_name\" into dj's system\n");
  printf("  s [-n <vertex>] [-c <vertex>] [-f] [-v] (stats)\n");
  printf("    [-n <vertex>] - prints all neighbors of specified vertex\n");
  printf("                  - if no vertex present, prints all neighbors\n");
  printf("    [-c <vertex>] - prints all connections of specified vertex\n");
  printf("                  - if no vertex present, prints all connections\n");
  printf("    [-f] - prints current working file\n");
  printf("    [-v] - prints all vertices in working file\n");
  printf("  c <vertex_1>, <vertex_2> (calculate)\n");
  printf("    displays shortest path between specified vertices\n");
  printf("    NOTE: the comma between vertex names is necessary\n"); /* #grader actually, the comma AND the space are necessary in your current implementation */
  printf("  exit\n");
  printf("    terminates execution of program\n");
  printf("============================================================\n");
  return;
}

/* returns 1 if read was unsuccesful, 2 if graph is empty, 0 otherwise */
int read(char *cmd)
{
  char *past_file = curr_file;
  if(strcmp("read", cmd) < 0){
    cmd = cmd + 5;
  } else {
    cmd = cmd + 2;
  }
  curr_file = strdup(cmd);

  if(fopen(curr_file, "r") == NULL){/* if file doesn't exit */
    free(curr_file);
    if(past_file != NULL){
      curr_file = strdup(past_file);
    } else {
      curr_file = NULL;
    }
    return 1;
  }

  /* parsing vertices */
  if(fgetc(fopen(curr_file, "r")) != '#'){/* if file isn't well formed */
    free(curr_file);                      /* NOTE: this isn't a very good test */
    if(past_file != NULL){
      curr_file = strdup(past_file);
    } else {
      curr_file = NULL;
    }
    return 2;
  }

  /* builds the machinery to perform dj calculate here */
  f = fopen(curr_file, "r");
  fscanf(f, "#vertices\n");
  if(t != NULL)
    htbl_free(t);
  t = htbl_init(79);
  sll *dj_sll = NULL;
  dj_sll = parse_vertices(t, f);

  if(dj_sll == NULL){
    printf("   -this is the empty graph\n");
    printf("   -there is no shortest distance to calculate\n");
    return 0;
  }

  size = dj_sll->i;
  dj_arr = sll_to_djtab_arr(dj_sll, size);

  /* parsing edges */
  fscanf(f, "edges\n");
  adj_mat = (edge_cost *)malloc(sizeof(edge_cost) * size * size);
  parse_edges(adj_mat, t, size, f);

  return 0;
}

/* returns NULL if no vertex name give */
char *extract_vertex(char *subcmd, int *done_nothing)
{
  *done_nothing = 0;
  int i;
  char vertex[512];
  subcmd += 2;
  if(subcmd[0] != '\0'){
    subcmd++;
    i = 0;
    if(*subcmd == '\0' || *subcmd == '-'){
      return NULL;
    } else {
      while(subcmd[i] != '\0' && subcmd[i] != '-'){
	vertex[i] = subcmd[i];
	i++;
      }
      if(vertex[i-1] == ' ')
	vertex[i-1] = '\0';
      vertex[i] = '\0';
    }
  } else {
    return NULL;
  }
  return strdup(vertex);
}
  

/* consider adding bonus arg that specifies which vertex */
void stats(char *cmd)/* if i, do both */
{
  int done_nothing = 1; /* has done nothing so far */
  char *subcmd;
  char *vertex;
  int i;
  int j;

  if(strcmp("stats", cmd) < 0){
    cmd += 6;
  } else {
    cmd += 2;
  }
  
  if((subcmd = strstr(cmd, "-n")) != NULL){/* neighbors command */
    vertex = extract_vertex(subcmd, &done_nothing);
    if(vertex == NULL){
      show_neighbors(adj_mat, dj_arr, size);
    } else if((i = htbl_find(t, vertex)) == -1){
      printf("   -error [-n \"vertex\"]: no such vertex\n");
      printf("   -try typing \"s -v \" for a list of vertices\n");
    } else {
      printf("neighbors of %s:\n", dj_arr[i]->name);
      for(j = 0; j < size; j++){
	if(adj_mat[(i * size) + j] != NULL){
	  printf("      %s\n", dj_arr[j]->name);
	}
      }
    }
    free(vertex);
  }
  if((subcmd = strstr(cmd, "-c")) != NULL){/* connections command */
    vertex = extract_vertex(subcmd, &done_nothing);
    if(vertex == NULL){
      show_connected(adj_mat, dj_arr, size);
    } else if((i = htbl_find(t, vertex)) == -1){
      printf("   -error [-c \"vertex\"]: no such vertex\n");
      printf("   -try typing \"s -v\" for a list of vertices\n");
    } else {
      show_one_connection(adj_mat, dj_arr, size, i);
    }
  }
  if(strstr(cmd, "-f") != NULL){/* current file command */
    done_nothing = 0;
    printf("********************************\n");
    if(curr_file != NULL){
      printf("working in file: %s\n", curr_file);
    } else {
      printf("no current working file\n");
    }
    printf("********************************\n");
  }
  if(strstr(cmd, "-v") != NULL){/* vertices command */
    done_nothing = 0;
    printf("current vertices:\n");
    for(i = 0; i < size; i++)
      printf("   %s\n", dj_arr[i]->name);
  }
  if(done_nothing)
    printf("   -error: unrecognized command %s\n", cmd);
  return;
}

/* calculate shortes path via dj algoithm */
void calculate(char *cmd)
{
  int i = 0;
  if(strcmp("calculate", cmd) < 0){
    cmd += 10;
  } else {
    cmd += 2;
  }
  for(i = 0; cmd[i] != ',' && cmd[i] != '\0'; i++)
    source[i] = cmd[i];
  source[i] = '\0';

  if(!strcmp(source, cmd)){
    printf("improperly calculate statement, type \"help\" for assisstance\n");
    return;
  }
  cmd += strlen(source) + 2;
  for(i = 0; cmd[i] != '\0'; i++){
    target[i] = cmd[i];
  }
  target[i] = '\0';

  printf("calculating shortest distance from %s to %s...\n", source, target);
  sll *path = dj_path(source, target, t, adj_mat, dj_arr, size);
  if(path != NULL)
    sll_show(path);
    
  return;
}

/* return value: 1 when user requests exit, 0 otherwise */
/* side effect: process given command */
int process_command(char *cmd)
{
  char *cmd_after;
  if (strcmp(cmd,"exit")==0){
    return 1;
  } else if (strcmp(cmd,"help")==0 || strcmp(cmd, "?") == 0){
    help();
  } else if (strcmp("read", cmd) == 0 || strcmp("r", cmd) == 0){
    printf("read what?\n");
  } else if (strcmp("read ", cmd) < -26 || strcmp("r ", cmd) < -26){
    int n = read(cmd);
    if(n == 1){
      printf("   -error: this file-name does not exist\n");
      return 0;
    } else if(n == 2){
      printf("   -error: this file is not a well formed .dwg file\n");
      return 0;
    } else{
      printf("********************************\n");
      printf("working in file: %s\n", curr_file);
      printf("********************************\n");
    }
  } else if (strcmp(cmd, "stats") == 0 || strcmp(cmd, "s") == 0){
    printf("usage: [-f] [-n] [-v] or [-c] required\n");
  } else if (strcmp("stats ", cmd) < -26 || strcmp("s ", cmd) < -26){
    if(curr_file == NULL){
      printf("must be working in a file first\n");
      return 0;
    }
    stats(cmd);
  } else if (strcmp("calculate", cmd) == 0 || strcmp("c", cmd) == 0){
    printf("calculate what?\n");
  } else if (strcmp("calculate ", cmd) < -26 || strcmp("c ", cmd) < -26){
    if(curr_file == NULL){
      printf("must be working in a file first\n");
      return 0;
    }
    calculate(cmd);
  } else {
    printf("command \"%s\" not found, try 'help' or '?'\n",cmd);
  }
  return 0;
}



commands.h
------------------
/* commands.h */


#ifndef _COMMANDS_H
#define _COMMANDS_H

void help();

void stats(char *cmd);

void calculate(char *cmd);

int read(char *cmd);

char *extract_vertex(char *subcmd, int *done_nothing);

int process_command(char *cmd);


sll *dj_path(char *source, char *target, htbl *t, 
	     edge_cost *adj_mat, dj_table *dj_arr, int size);


#endif /* _COMMANDS_H */


dj.c
------------------
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


dj.h
------------------
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


hash-table.c
------------------
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


hash-table.h
------------------
#ifndef _HASH_TABLE_H
#define _HASH_TABLE_H

#include "linked-list.h"

/* hash table of strings, with linked list buckets */

struct hash_table {
  int n_buckets;
  sll **buckets;
};

typedef struct hash_table htbl;

/* hash : char -> unsigned int */
/* compute hash code for given string */
unsigned long hash(char *s);

/* htbl_init : int -> htbl* */
/* allocate space for a new hash table of given size */
/* all buckets must initially contain the empty list */
htbl *htbl_init(int sz);

/* htbl_add : (htbl*, char*) -> int */ 
/* add string s to hast table t */
/* return the number of strings in s's bucket _after_ inserting it */
int htbl_add(htbl *t, char *name, int done, int dist, char *pred, char *edge, int i);

/* htbl_member : (htbl*, char*) -> int */
/* test membership of given string in given table */
/* the integer returned is a (pseudo) boolean */
int htbl_member(htbl *t, char *s);

/* htbl_show : htbl* -> <void> */
/* print a represntation of the hash table to stdout */
void htbl_show(htbl *t);

/* htbl_find : (htbl*, char*) -> int */
/* finds a vertex name, returns its corresponding array index */
/* return -1 if not found */
int htbl_find(htbl *t, char* vertex);

/* frees a hash table */
void htbl_free(htbl *t);

#endif /* _HASH_TABLE_H */


linked-list.c
------------------
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
void sll_show(sll *ss)
{
  int curr_dist;
  if(ss == NULL){
    printf("you are at your destination\n");
    return;
  }
  printf("From %s, ", ss->dj->name);
  curr_dist = ss->dj->dist;
  ss = ss->next;
  while(ss != NULL){
    printf("go along \"%s\" (cost: %d) to \"%s\".\nFrom \"%s\", ", 
	   ss->dj->edge, ss->dj->dist - curr_dist, 
	   ss->dj->name, ss->dj->name);
    curr_dist = ss->dj->dist;
    ss = ss->next;
  }
  printf("go nowhere because you have arrived!\n");
  printf("The total cost was %d.\n", curr_dist);
  return;
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


linked-list.h
------------------
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


main.c
------------------
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


main.h
------------------
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


parse.c
------------------
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



parse.h
------------------
/* Kevin Rose, kbrose */
/* CS 152 Winter 2012 */
/* lab 8 */

sll *parse_vertices(htbl *t, FILE *f);

void parse_edges(edge_cost *adj_mat, htbl *t, int size, FILE *f);

/* converts a string linked list to an array of exact size */
dj_table *sll_to_djtab_arr(sll *vert_sll, int size);


utils.c
------------------
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


utils.h
------------------
/* utils.h */

#ifndef _UTILS_H
#define _UTILS_H

/* allocate space for new string, initialize all chars to '\0' */
char *string_init(int sz);

/* return new string stripped of leading and trailing spaces */
/*   (including \n and \t) */
char *trim(char *s);

#endif /* _UTILS_H */


vert-edge.c
------------------
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


vert-edge.h
------------------
/* Kevin Rose, kbrose */
/* CS 152 Winter 2012 */
/* lab 8 */
/*
struct name_num{
  char *name;
  int n;
};

/*typedef struct name_num *name_num;

  name_num new_name_num(char *name, int n);*/

struct edge_cost{
  char *edge;
  int cost;
};

typedef struct edge_cost *edge_cost;

edge_cost new_edge_cost(char *edge, int cost);

void show_connected(edge_cost *adj_mat, dj_table *dj_arr, int size);

void show_neighbors(edge_cost *adj_mat, dj_table *dj_arr, int size);

void show_one_connection(edge_cost *adj_mat, dj_table *dj_arr, int size, int i);


/* reads/builds graph        3/ 3 */
/* shortest-path correctness 8/ 8 */
/* code design/organization  8/ 8 */
/* user experience           4/ 4 */
/* Makefile                  1/ 1 */
/* svn                       1/ 1 */
/* style                     5/ 5 */
/* #total                    30/30 */
