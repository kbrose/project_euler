#include <stdio.h>

int col(unsigned long int i, int arr[2000000])
{
  int counter = 0;

  while(i > 1999999 || arr[i] == -1){
    if(!(i % 2)){
      i = i / 2;
    } else {
      i = (i * 3) + 1;
    }
    counter++;
  }
    
  
  return arr[i] + counter;
}

int main()
{
  long unsigned n;
  int counter = 0;
  int arr[2000000];
  int currnum = 0;
  int currind;
  unsigned long int i;

  for(i = 0; i < 2000000; i++){
    arr[i] = -1;
  }
  arr[1] = 0;
  
  for(i = 1; i < 1000000; i++){
    arr[i] = col(i, arr);
    if(arr[i] > currnum){
      currnum = arr[i];
      currind = i;
    }
  }
  printf("%d\n", currind);
 
  return 0;
}
