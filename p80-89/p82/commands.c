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
  printf("    NOTE: the comma between vertex names is necessary\n");
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
  int i,j,curr_min;
  if(strcmp("calculate", cmd) < 0){
    cmd += 10;
  } else {
    cmd += 2;
  }
  /*
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
  */

  sll *path;
  int adder;
  int starters[80] = {4445,1096,9607,7206,3620,1074,4295,510,9444,3327,6882,7338,4420,356,9870,192,1046,4659,5759,1571,1822,8738,7047,3975,9248,5093,6237,9905,5825,6223,5826,1861,4052,4629,8316,2341,6430,2810,6206,3847,5458,3266,1998,8878,3637,8497,8188,9935,3466,1005,7280,9517,7444,3287,1772,126,8074,7845,4164,4258,7854,7178,6957,4417,9284,3787,2650,3101,4865,171,3744,2810,7096,8830,2738,6044,8478,2265,2132,5304};
  curr_min = 421365;
  for(i = 0; i < 80; i++){
    adder = starters[i];
    for(j = 0; j < 80; j++){
      printf("%d\t%d\n", i, j);
      sprintf(source,"%d:0",i);
      sprintf(target,"%d:79",j);
      path = dj_path(source,target,t,adj_mat,dj_arr,size);
      if (sll_show(path) + adder < curr_min) {
	curr_min = sll_show(path) + adder;
      }
    }
  }
  printf("curr_min: %d\n", curr_min);

  /*printf("calculating shortest distance from %s to %s...\n", source, target);*/
  //sll *path = dj_path(source, target, t, adj_mat, dj_arr, size);
  //if(path != NULL)
  //  printf("%d\n", sll_show(path));
    
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

