#include <stdio.h>
#include <stdlib.h>

#define MIL 1000000

int sum_prop_divisors(int n)
{
  int i, end, sum, divider;
  sum = 1; /* all numbers are divisible by 1 */
  end = (n >> 1) + 1;
  for (i = 2; i < end; i++){
    if (!(n % i)){
      sum += i;
      divider = n / i;
      if (divider != i){
	sum += divider;
      }
      end = divider;
    }
  }
  return sum;
}

int test(int n)
{
  printf("\n\tHERE %d\n\n", n);
  return 0;
}

int main()
{
  int curr_num, i, j, branch, curr_chain_len, big_chain_len, temp, STOP;
  int *arr = (int *) malloc (sizeof(int) * 3 * MIL);
  for (i = 0; i < 3 * MIL; i++){
    arr[i] = 0;
  }
  branch = 1;
  curr_chain_len = 0;
  for (i = 1; i < MIL; i++){
    temp = i;
    STOP = 0;
    while (!arr[i]){ /* already visited this number */
      arr[i] = 1;
      arr[MIL + i] = branch;
      arr[(2 * MIL) + i] = curr_chain_len;
      curr_chain_len++;
      i = sum_prop_divisors(i);
      if (i >= MIL){
	STOP = 1;
	break;
      }
    }
    
    if (STOP){
      i = temp;
      curr_chain_len = 0;
      branch++;
      continue;
    }

    if (branch == arr[MIL + i]){ /* haven't covered this branch before */
      if ((curr_chain_len - arr[(2 * MIL) + i]) > big_chain_len){ /* biggest chain */
  	big_chain_len = curr_chain_len - arr[(2 * MIL) + i];
	curr_num = i;
	j = i;
	do { /* make curr_num the lowest element in the chain */
	  printf("%d --> ", j);
	  if (j < curr_num){
	    curr_num = j;
	  }
	  j = sum_prop_divisors(j);
	} while (j != i);
	printf("%d\n\n", j);
      }
    }
    curr_chain_len = 0;
    branch++;
    i = temp;
    /*
    printf("i: %d\n", i);
    printf("curr_num: %d\n", curr_num);
    printf("branch: %d\n\n", branch);
    */
  }
  printf("answer: %d\n", curr_num);
  return 0;
}
