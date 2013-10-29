#include <stdio.h>

int main()
{
  int numOfLines = 15;
  int n;
  int arr[15];
  int i;

  for(i = 0; i < numOfLines; i++){
    scanf("%d ", &n);
    arr[i] = n;
  }
  numOfLines--;
  
  while(numOfLines > 0){
    for(i = 0; i < numOfLines; i++){
      scanf("%d ", &n);
      arr[i] = n + (arr[i] > arr[i+1] ? arr[i] : arr[i+1]);
    }
    numOfLines--;
  }

  printf("sum: %d\n", arr[0]);
  
  return 0;
}
