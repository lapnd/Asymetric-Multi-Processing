//
// Created by jofaye on 20/06/22.
//

#include <stdio.h>
#include <stdlib.h>

typedef struct DATA {
    int flag;
    int value;
} DATA;

void sum(void) ;

int b __attribute__ ((section("sink"))) = 3;
DATA data __attribute__ ((section ("joseph")));

void sum(void)
{
    int a = 1 ;

    printf("Hello Maxime and Jean-Francois :D, I Am FemtorV, I Get A Value From FireV");
    printf(": %d \n", data.value);
    printf("The value in the sink section (scratchpad memory), is equal to : %d \n", b);

    if (data.flag == 1)
        {
          b = a + data.value;
          printf("I compute a sum operation.\nFemtorv Sum: %d \n", b);
          data.flag = 0;
        }
}