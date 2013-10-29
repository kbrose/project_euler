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
