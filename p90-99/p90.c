#include <stdio.h>

int can_make_n(int n1, int n2, int d1[], int d2[])
{
  int i = 0;
  int n1_in_d1 = 0;
  int n2_in_d1 = 0;
  int n1_in_d2 = 0;
  int n2_in_d2 = 0;
  int d_1, d_2;
  //int temp;
  //int bool_69 = 0;

  /*
  if ((n2 == 6) || (n2 == 9)){ 
    temp = n2;
    n2 = n1;
    n1 = temp;
  }
  */
  //if ((n1 == 6) || (n1 == 9))
  //  bool_69 = 1;

  for (i = 0; i < 6; i++){
    d_1 = d1[i];
    d_2 = d2[i];
    if (d_1 == n1)
      n1_in_d1 = 1;
    if (d_1 == n2)
      n2_in_d1 = 1;
    if (d_2 == n1)
      n1_in_d2 = 1;
    if (d_2 == n2)
      n2_in_d2 = 1;

    if (d_1 == 6)
      if (n1 == 9)
	n1_in_d1 = 1;
    if (d_1 == 9)
      if (n1 == 6)
	n1_in_d1 = 1;
    if (d_2 == 6)
      if (n1 == 9)
	n1_in_d2 = 1;
    if (d_2 == 9)
      if (n1 == 6)
	n1_in_d2 = 1;
  }

  return (n1_in_d1 && n2_in_d2) || (n2_in_d1 && n1_in_d2);
}

int main()
{
  int d10,d11,d12,d13,d14,d15;
  int d20,d21,d22,d23,d24,d25;
  int counter = 0;
  int d1[6];
  int d2[6];

  for (d10 = 0; d10 < 5; d10++){
    d1[0] = d10;
    for (d11 = d10+1; d11 < 6; d11++){
      d1[1] = d11;
      for (d12 = d11+1; d12 < 7; d12++){
	d1[2] = d12;
	for (d13 = d12+1; d13 < 8; d13++){
	  d1[3] = d13;
	  for (d14 = d13+1; d14 < 9; d14++){
	    d1[4] = d14;
	    for (d15 = d14+1; d15 < 10; d15++){
	      d1[5] = d15;
	      for (d20 = 0; d20 < 5; d20++){
		d2[0] = d20;
		for (d21 = d20+1; d21 < 6; d21++){
		  d2[1] = d21;
		  for (d22 = d21+1; d22 < 7; d22++){
		    d2[2] = d22;
		    for (d23 = d22+1; d23 < 8; d23++){
		      d2[3] = d23;
		      for (d24 = d23+1; d24 < 9; d24++){
			d2[4] = d24;
			for (d25 = d24+1; d25 < 10; d25++){
			  d2[5] = d25;
			  if (can_make_n(0,1,d1,d2) &&
			      can_make_n(0,4,d1,d2) &&
			      can_make_n(9,0,d1,d2) &&
			      can_make_n(6,1,d1,d2) &&
			      can_make_n(2,5,d1,d2) &&
			      can_make_n(6,3,d1,d2) &&
			      can_make_n(9,4,d1,d2) &&
			      can_make_n(6,4,d1,d2) &&
			      can_make_n(8,1,d1,d2))
			    counter++;
			}
		      }
		    }
		  }
		}
	      }
	    }
	  }
	}
      }
    }
  }

  printf("%d\n", counter/2);
  
  return 0;
}
