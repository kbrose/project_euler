#include <stdio.h>

void swap(char arr[50][5200], int j)
{
  char temp[50];
  int i;
  for(i = 0; arr[i][j] != '\0'; i++)
    temp[i] = arr[i][j];
  temp[i] = '\0';

  for(i = 0; arr[i][j+1] != '\0'; i++)
    arr[i][j] = arr[i][j+1];
  arr[i][j] = '\0';

  for(i = 0; temp[i] != '\0'; i++)
    arr[i][j+1] = temp[i];
  arr[i][j+1] = '\0';
}

void sort(char arr[50][5200])
{
  int swaps_bool = 1;
  int i, j;
      
  while(swaps_bool){
    swaps_bool = 0;
    for(j = 0; j < 5162; j++)
      for(i = 0; i < 50; i++){
	if(arr[i][j] == '\0')
	  break;
	if(arr[i][j+1] == '\0'){
	  swaps_bool = 1;
	  swap(arr, j);
	  break;
	}
	if(arr[i][j] < arr[i][j+1])
	  break;
	if(arr[i][j] > arr[i][j+1]){
	  swaps_bool = 1;
	  swap(arr, j);
	  break;
	}
      }
  }
}

long int count(char arr[50][5200])
{
  long int accum = 0;
  int score;
  int i, j;
  for(i = 0; i < 5200; i++){
    score = 0;
    for(j = 0; j < 50 && (arr[j][i] != '\0'); j++)
      score += arr[j][i];
    accum += (score * (i+1));
  }
   
  return accum;
}

int main()
{
  char name[50];
  long int sum;
  char arr[50][5200];
  int i, j;

  j = 0;
  while((scanf("%s ", name)) != EOF){
    for(i = 0; name[i] != '\0'; i++)
      arr[i][j] = name[i] - 64;
    j++;
  }

  sort(arr);

  sum = count(arr);

  printf("sum: %ld\n", sum);

  return 0;
}
