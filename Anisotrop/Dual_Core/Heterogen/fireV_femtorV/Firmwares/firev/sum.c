//
// Created by jofaye on 20/06/22.
//

#include <stdio.h>
#include <stdlib.h>

typedef struct DATA {
    int flag;
    int value;
} DATA;

void sum(void);

DATA data __attribute__ ((section ("joseph"))) = {0,  0};
int a __attribute__ ((section ("source"))) = 1;

void sum(void)
{
    int b = 1;
    printf("Hello Maxime and Jeff, I am FireV\n");
    printf("The initial value in the source is :%d\n", a);
    printf("Initial value of data in shared mem is :%d\n", data.value);
        if (data.flag == 0)
        {
            data.value = a + b;
            printf("I've computed : %d\n", data.value);
            a +=1 ;
            data.flag = 1;
        }
}
