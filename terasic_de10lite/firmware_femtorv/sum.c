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

int a ;
int b ;

DATA data __attribute__ ((section ("joseph"))) ;

void sum(void)
{
    int a=1;
    int b=0;
    printf("hello I am the femtorv, I get that from firev");
    printf("Firev sum: %d \n", data.value);

       if (data.flag == 1)
        {
          b = a + data.value;
          printf("femtorv sum: %d \n", b);

          data.flag = 0;
        }

}