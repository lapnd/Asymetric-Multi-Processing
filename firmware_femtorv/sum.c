//
// Created by jofaye on 20/06/22.
//

#include <stdio.h>
#include <stdlib.h>

typedef struct DATA {
    int flag;
    int value;
} DATA;

int a ;
int b ;

DATA data __attribute__ ((section ("joseph"))) = {0,  0};

void sum()
{
    int a=1;
    int b=0;
    printf("Firev sum: %d", data.value);
    while(1)
    {
       if (data.flag == 1)
        {
          b = a + data.value;
          printf("femtorv sum: %d", b);
          data.flag = 0;
        }
    }
}