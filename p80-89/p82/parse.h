/* Kevin Rose, kbrose */
/* CS 152 Winter 2012 */
/* lab 8 */

sll *parse_vertices(htbl *t, FILE *f);

void parse_edges(edge_cost *adj_mat, htbl *t, int size, FILE *f);

/* converts a string linked list to an array of exact size */
dj_table *sll_to_djtab_arr(sll *vert_sll, int size);
