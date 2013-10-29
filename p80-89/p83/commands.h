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
