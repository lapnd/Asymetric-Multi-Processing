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
int a ;
int b ;

DATA data __attribute__ ((section ("joseph"))) = {0,  0};

void sum(void)
{
    printf("Hello I am fireV; initial value is %d ", data.value);
    a = 2;
    b = 1;
        if (data.flag == 0)
        {
            data.value = a + b;
            a +=1 ;
            data.flag = 1;
            printf("I've computed : %d", data.value);
        }

}
